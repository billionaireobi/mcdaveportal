# Django core imports
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from django.core.mail import EmailMessage
from django.conf import settings
from django.http import JsonResponse

from django.views.decorators.csrf import csrf_exempt

# Python standard library imports
from datetime import datetime
import json

# Local imports
from .models import *  # It's better to explicitly import what you need

# create your vies here 
def log_in_user(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None and user == request.user:
            login(request,user)
            messages.success(request,"Login successful! Welcome back.")
            return redirect('hrms')
        else:
            messages.error(request,"Invalid username or password. Please try again.")
            return redirect('log-in')
    
    return render(request,"hrms/authenticate/login.html")

def logout_view(request):
    logout(request)
    messages.success(request, 'You have been successfully logged out.')
    return redirect('log-in')

def forgetpassword(request):
    if request.method== 'POST':
        email=request.POST.get('email')
        # verify email
        try:
            user=User.objects.get(email=email)
            new_password_reset = passwordreset(user=user)
            new_password_reset.save()
            # generate url
            password_reset_url=reverse('resetpassword', kwargs={'reset_id':new_password_reset.reset_id})
            full_password_reset=f'{request.scheme}://{request.get_host()}{password_reset_url}'
            email_body=f'Reset your Password Using the link below:\n\n{full_password_reset}'
            
            email_message=EmailMessage(
                'Reset Your Password',#subject
                email_body,
                settings.EMAIL_HOST_USER,#sender
                [email]
            )
            email_message.fail_silently=True
            email_message.send()
            # messages.success(request, "Password reset email sent successfully.")
            # return redirect('forgetpassword') 
            messages.success(request, "Password reset email sent successfully.")
            return redirect('passwordreset', reset_id=new_password_reset.reset_id)
        except User.DoesNotExist:
            messages.error(request,f"No user with email {email} was found")
            return redirect('forgetpassword')
    return render(request, 'authentication/forget_password.html')

def passwordresetsent(request,reset_id):
    if passwordreset.objects.filter(reset_id=reset_id).exists():
         return render(request, 'authentication/passwordreset_done.html')
    else:
        messages.error(request, 'Invalid reset Id')
        return redirect('forgetpassword')


def resetpassword(request, reset_id):
    try:
        password_reset = passwordreset.objects.get(reset_id=reset_id)
        current_time = timezone.now()
        # Check for link expired
        passwords_have_error = True
        # expiration_time = password_reset.created_when + timezone.timedelta(minutes=10)
        expiration_time = password_reset.created_when + timezone.timedelta(minutes=10)   
        if current_time > expiration_time:
            # print(f"Link expired at: {expiration_time}") 
            passwords_have_error = True
            messages.error(request, "Reset Link Has Expired")
            # Delete reset id if expired
            
            password_reset.delete()
            # return render(request, 'authentication/link_expired.html')
            return redirect('sign-in')
            
        if request.method == 'POST':
            password = request.POST.get('password')
            confirmpassword = request.POST.get('confirm_password')
            
            passwords_have_error = False
            
            if password != confirmpassword:
                passwords_have_error = True
                messages.error(request, "The two Password Fields Did Not Match!")
            
            if len(password) < 8:
                passwords_have_error = True
                messages.error(request, "Password Must Be At least 8 Characters Long!")
            
            
            if not passwords_have_error:
                user = password_reset.user
                user.set_password(password)
                user.save()
                # Delete reset id after use
        
                messages.success(request, "Password reset successfully!!")
                password_reset.delete()
                return redirect('password_reset_complete')
            
        # If this is a GET request or if there were password errors, render the form
        return render(request, 'authentication/resetpassword.html', {
            'reset_id': reset_id  # Add this line to pass the reset_id to the template
        })
            
    except passwordreset.DoesNotExist:
        # messages.error(request, 'Invalid Reset Link Please get another!!')
        return render(request, 'authentication/link_expired.html')
@login_required(login_url='/log-in/')  
def hrms_page(request):
    return render(request, "hrms/dashboards/index.html")


@login_required(login_url='/login/')
def calendar_view(request):
    try:
        events = Event.objects.filter(user=request.user)
        upcoming_events = events.filter(
            start__gte=timezone.now()
        ).order_by('start')[:5]
        
        return render(request, "calendar/calendar.html", {
            'upcoming_events': upcoming_events
        })
    except Exception as e:
        return render(request, "calendar/calendar.html", {
            'error': str(e),
            'upcoming_events': []
        })

@login_required
def get_events(request):
    events = Event.objects.filter(user=request.user)
    events_list = [{
        'id': event.id,
        'title': event.title,
        'start': event.start.isoformat(),
        'end': event.end.isoformat() if event.end else None,
        'description': event.description
    } for event in events]
    return JsonResponse(events_list, safe=False)

@login_required
@csrf_exempt
def add_event(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            event = Event.objects.create(
                user=request.user,
                title=data['title'],
                description=data.get('description', ''),
                start=datetime.fromisoformat(data['start'].replace('Z', '+00:00')),
                end=datetime.fromisoformat(data['end'].replace('Z', '+00:00')) if data.get('end') else None
            )
            return JsonResponse({
                'id': event.id,
                'title': event.title,
                'description': event.description,
                'start': event.start.isoformat(),
                'end': event.end.isoformat() if event.end else None,
            }, status=201)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        except KeyError as e:
            return JsonResponse({'error': f'Missing required field: {str(e)}'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({'error': 'Invalid request method'}, status=405)

@login_required
@csrf_exempt
def update_event(request, event_id):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            event = get_object_or_404(Event, id=event_id, user=request.user)
            event.title = data['title']
            event.description = data.get('description', '')
            event.start = datetime.fromisoformat(data['start'].replace('Z', '+00:00'))
            event.end = datetime.fromisoformat(data['end'].replace('Z', '+00:00')) if data.get('end') else None
            event.save()
            return JsonResponse({
                'id': event.id,
                'title': event.title,
                'description': event.description,
                'start': event.start.isoformat(),
                'end': event.end.isoformat() if event.end else None,
            })
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        except KeyError as e:
            return JsonResponse({'error': f'Missing required field: {str(e)}'}, status=400)
        except Event.DoesNotExist:
            return JsonResponse({'error': 'Event not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({'error': 'Invalid request method'}, status=405)

@login_required
@csrf_exempt
def delete_event(request, event_id):
    if request.method == 'DELETE':
        try:
            event = get_object_or_404(Event, id=event_id, user=request.user)
            event.delete()
            return JsonResponse({'success': True}, status=204)
        except Event.DoesNotExist:
            return JsonResponse({'error': 'Event not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({'error': 'Invalid request method'}, status=405)
from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import *
from django.db.models import Sum, F, Func, IntegerField
from django.db.models.functions import Cast, TruncMonth
from datetime import datetime
from django.http import JsonResponse
from .models import*

# Create your views here.
def index(request):
    return render(request,"dashboards/landingpage.html")

def sign_in_user(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"Login successful! Welcome back.")
            return redirect('home')
        else:
            messages.error(request,"Invalid username or password. Please try again.")
            return redirect('sign-in')
    else:
        return render(request,"authentication/loginuser.html")

def sign_out_user(request):
    logout(request)
    messages.success(request,"you logged out")
    return redirect('sign-in')

def sign_up_user(request):
    if request.method=='POST':
       form=SignUpForm(request.POST) 
       if form.is_valid():
            form.save()
            # authenticate and log in
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            user=authenticate(username=username,password=password)
            login(request,user)
            messages.success(request,'you have succesfully registered')
            return redirect('sign-in')
    else:
        form=SignUpForm()
        return render(request,'authentication/signin.html',{'form':form})
    return render(request,'authentication/signin.html',{'form':form})
# analytics dashboard

@login_required(login_url='/sign-in/')   
def home_page(request):
    return render(request, 'dashboards/analytics.html')
@login_required(login_url='/sign-in/')
def get_monthly_production_data(request):
    try:
        # Use Django ORM to group by month
        data = (
            PackingData.objects.annotate(
                month=TruncMonth('date'),  # Group by month
                total_quantity=Cast(F('achieved'), IntegerField()) * 24
            )
            .values('month')
            .annotate(total=Sum('total_quantity'))
            .order_by('month')
        )

        # Format the month for display (e.g., 'December 2024')
        formatted_data = [
            {
                "month": entry["month"].strftime("%B %Y"),  # Properly format date
                "total": entry["total"]
            }
            for entry in data
        ]

        return JsonResponse(formatted_data, safe=False)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
# production views
# csrqs view
@login_required(login_url='/sign-in/')
def production_crqs(request):
    records=CRQSData.objects.all()
    return render(request,"dashboards/crqs.html",{'records':records})
        
        
        # add record view
@login_required(login_url='/sign-in/')
def addrecord(request):
    form = AddRecordForm(request.POST or None)  # Initialize form
    
    if request.method == "POST":  # Handle form submission
        if form.is_valid():
            form.save()
            messages.success(request, "Record added successfully!")
            return redirect("crqs-info")
        else:
            messages.error(request, "There were errors in your form. Please fix them.")

    # Render the form template
    return render(request, "forms/crqs/crqsaddrecord.html", {"form": form})
# view individualrecord 
@login_required(login_url='/sign-in/')
def view_record(request, pk):
    if request.user.is_authenticated:
        crqsrecord=CRQSData.objects.get(id=pk)
        return render(request, "forms/crqs/crqsviewrecord.html", {"crqsrecord": crqsrecord})
    else:
        messages.success(request,'you need to login to view this page')
        return redirect('sign-in')

# delete record view
@login_required(login_url='/sign-in/')
def delete_record(request,pk):
    delete_it=CRQSData.objects.get(id=pk)
    delete_it.delete()
    messages.success(request,'Record Deleted successfully!!')
    return redirect('crqs-info')    
# UPDATE RECORDVIEW
@login_required(login_url='/sign-in/')
def update_record(request,pk):
    if request.user.is_authenticated:
        current_record=CRQSData.objects.get(id=pk)
        form=AddRecordForm(request.POST or None,instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request,"Record Has Been Updated!!")
            return redirect("crqs-info")
        return render(request,"forms/crqs/crqsupdaterecords.html",{"form":form})
    else:
        messages.success(request,"You must be logged in")
        return redirect("sign-in")
    # endof crqsviews
    # start of packing views
@login_required(login_url='/sign-in/')
def packing_info(request):
    records=PackingData.objects.all()
    return render(request,"dashboards/packing.html",{'records':records})
    # packing add records
@login_required(login_url='/sign-in/')
def packing_record(request):
    form = PackRecordForm(request.POST or None)  # Initialize form
    
    if request.method == "POST":  # Handle form submission
        if form.is_valid():
            form.save()
            messages.success(request, "Record added successfully!")
            return redirect("packing-info")
        else:
            messages.error(request, "There were errors in your form. Please fix them.")

    # Render the form template
    return render(request, "forms/packing/addrecord.html", {"form": form})
    
# packing view record
@login_required(login_url='/sign-in/')
def packingviewrecord(request,pk):
    if request.user.is_authenticated:
        packrecord=PackingData.objects.get(id=pk)
        return render(request, "forms/packing/packviewrecord.html", {"packrecord": packrecord})
    else:
        messages.success(request,'you need to login to view this page')
        return redirect('sign-in')
# update packing record
@login_required(login_url='/sign-in/')
def packupdate_record(request,pk):
    if request.user.is_authenticated:
        current_record=PackingData.objects.get(id=pk)
        form=PackRecordForm(request.POST or None,instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request,"Record Has Been Updated!!")
            return redirect("packing-info")
        return render(request,"forms/packing/packupdaterecord.html",{"form":form})
    else:
        messages.success(request,"You must be logged in")
        return redirect("sign-in")
       
#delete record for packing
@login_required(login_url='/sign-in/')
def packdelete_record(request,pk):
    delete_it=PackingData.objects.get(id=pk)
    delete_it.delete()
    messages.success(request,'Record Deleted successfully!!')
    return redirect('packing-info')
      
    # production mixing views
@login_required(login_url='/sign-in/')
def production_mixing(request):
    return render(request,"dashboards/mixing.html")
# vlemonke view
@login_required(login_url='/sign-in/')
def production_vlemonke(request):
    records=VimLemonKe.objects.all()
    return render(request,"productionprocessing/vimproductke/vlemonke.html",{'records':records})
# vlemon add record
@login_required(login_url='/sign-in/')
def addrecordvlemon(request):
    form = VimLemonForm(request.POST or None)  # Initialize form
    
    if request.method == "POST":  # Handle form submission
        if form.is_valid():
            form.save()
            messages.success(request, "Record added successfully!")
            return redirect("vlemonke")
        else:
            messages.error(request, "There were errors in your form. Please fix them.")

    # Render the form template
    return render(request, "productionprocessing/vimproductke/vlemonaddrecord.html", {"form": form})
# vlemonke viewrecord
@login_required(login_url='/sign-in/')
def viewrecordvlemon(request,pk):
    if request.user.is_authenticated:
        viewrecord=VimLemonKe.objects.get(id=pk)
        return render(request, "productionprocessing/vimproductke/vimviewrecord.html", {"viewrecord": viewrecord})
    else:
        messages.success(request,'you need to login to view this page')
        return redirect('sign-in')
    # update record vlemonke
@login_required(login_url='/sign-in/')
def updaterecordvlemon(request,pk):
    if request.user.is_authenticated:
        current_record=VimLemonKe.objects.get(id=pk)
        form=VimLemonForm(request.POST or None,instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request,"Record Has Been Updated!!")
            return redirect("vlemonke")
        return render(request,"productionprocessing/vimproductke/vimupdaterecord.html",{"form":form})
    else:
        messages.success(request,"You must be logged in")
        return redirect("sign-in")
# delete record vlemonke
@login_required(login_url='/sign-in/')
def deleterecordvlemon(request,pk):
    delete_it=VimLemonKe.objects.get(id=pk)
    delete_it.delete()
    messages.success(request,'Record Deleted successfully!!')
    return redirect('vlemonke')
# vimlavender production
@login_required(login_url='/sign-in/')
def production_vlavenderke(request):
    records=VimLavenderKe.objects.all()
    return render(request,"productionprocessing/vimlavender/vlavenderke.html",{'records':records})
# addrecord vimlavender
@login_required(login_url='/sign-in/')
def addrecordvlavenderke(request):
    form = VimLavenderForm(request.POST or None)  # Initialize form
    
    if request.method == "POST":  # Handle form submission
        if form.is_valid():
            form.save()
            messages.success(request, "Record added successfully!")
            return redirect("vlavenderke")
        else:
            messages.error(request, "There were errors in your form. Please fix them.")

    # Render the form template
    return render(request, "productionprocessing/vimlavender/vlavenderaddrecord.html", {"form": form})
# viewrecord lavender
@login_required(login_url='/sign-in/')
def viewrecordvlavenderke(request,pk):
    if request.user.is_authenticated:
        viewrecord=VimLavenderKe.objects.get(id=pk)
        return render(request, "productionprocessing/vimlavender/lavenderviewrecord.html", {"viewrecord": viewrecord})
    else:
        messages.success(request,'you need to login to view this page')
        return redirect('sign-in')
    # updaterecord lavender
@login_required(login_url='/sign-in/')    
def updaterecordvlavenderke(request,pk):
    if request.user.is_authenticated:
        current_record=VimLavenderKe.objects.get(id=pk)
        form=VimLavenderForm(request.POST or None,instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request,"Record Has Been Updated!!")
            return redirect("vlavenderke")
        return render(request,"productionprocessing/vimlavender/lavenderupdaterecord.html",{"form":form})
    else:
        messages.success(request,"You must be logged in")
        return redirect("sign-in")
# deleterecord
@login_required(login_url='/sign-in/') 
def deleterecordvlavender(request,pk):
    delete_it=VimLavenderKe.objects.get(id=pk)
    delete_it.delete()
    messages.success(request,'Record Deleted successfully!!')
    return redirect('vlavenderke')
    
    
    

    

    
            

from django.contrib.auth import views as auth_views
from . import views
from django.urls import path,include

urlpatterns = [
    # homeview
    path("log-in/",views.log_in_user,name="log-in"),
    path('logging-out_user/', views.logout_view, name='logging-out_user'),
    # passwordreset
    path('forgetpassword/', views.forgetpassword, name='forgetpassword'),
    path('passwordreset/<str:reset_id>/', views.passwordresetsent, name='passwordreset'),
    path('resetpassword/<str:reset_id>/', views.resetpassword, name='resetpassword'),
    # path("link_expired/",views.link_expired,name="link_expired"),
    
    # calendar
    
    path('calendar/', views.calendar_view, name='calendar'),
    path('get_events/', views.get_events, name='get_events'),
    path('add_event/', views.add_event, name='add_event'),
    path('update_event/<int:event_id>/', views.update_event, name='update_event'),
    path('delete_event/<int:event_id>/', views.delete_event, name='delete_event'),
    # calendar
    path("hrms/",views.hrms_page,name="hrms"),
    #  # djangos default authentication urls
    path('accounts/', include('django.contrib.auth.urls')),
    # # password reset urls
    path('passwordreset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='authentication/passwordreset_complete.html'), name='password_reset_complete'),
    
]
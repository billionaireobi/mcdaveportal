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
    path('calendar/', views.calendar_view, name='calendar'),
    path("hrms/",views.hrms_page,name="hrms"),
    #  # djangos default authentication urls
    path('accounts/', include('django.contrib.auth.urls')),
    # # password reset urls
    path('passwordreset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='authentication/passwordreset_complete.html'), name='password_reset_complete'),
    
]
from django.contrib.auth import views as auth_views
from . import views
from django.urls import path,include

urlpatterns = [
    # homeview
    path("log-in/",views.log_in_user,name="log-in"),
    path('logout/', views.logout_view, name='logout'),
    # passwordreset
    path('forgetpassword/', views.forgetpassword, name='forgetpassword'),
    path('passwordreset/<str:reset_id>/', views.passwordresetsent, name='passwordreset'),
    path('resetpassword/<str:reset_id>/', views.resetpassword, name='resetpassword'),
    path('calendar/', views.calendar_view, name='calendar'),
    path("hrms/",views.hrms_page,name="hrms"),
    #  # djangos default authentication urls
    path('accounts/', include('django.contrib.auth.urls')),
    # # password reset urls
    
    # path('passwordreset/', auth_views.PasswordResetView.as_view(
    # template_name='authentication/password_reset_form.html',
    # success_url=reverse_lazy('passwordreset_done')
    # ), name='passwordreset'),
    # path('passwordreset_done/', auth_views.PasswordResetDoneView.as_view(template_name='authentication/passwordreset_done.html'), name='passwordreset_done'),
    # path('passwordreset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='authentication/passwordreset_confirm.html'), name='password_reset_confirm'),
    path('passwordreset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='authentication/passwordreset_complete.html'), name='password_reset_complete'),
    
]
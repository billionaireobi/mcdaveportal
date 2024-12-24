from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

urlpatterns = [
    # homeview
    path("",views.index,name=""),
    path('sign-in/', views.sign_in_user, name='sign-in'),
    path('sign-out/',views.sign_out_user,name='sign-out'),
    # djangos default authentication urls
    path('accounts/', include('django.contrib.auth.urls')),
    # password reset urls
    path('passwordreset/', auth_views.PasswordResetView.as_view(
    template_name='authentication/password_reset_form.html',
    success_url=reverse_lazy('passwordreset_done')
    ), name='passwordreset'),
    path('passwordreset_done/', auth_views.PasswordResetDoneView.as_view(template_name='authentication/passwordreset_done.html'), name='passwordreset_done'),
    path('passwordreset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='authentication/passwordreset_confirm.html'), name='password_reset_confirm'),
    path('passwordreset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='authentication/passwordreset_complete.html'), name='password_reset_complete'),
    # email activation urls
    path('activate/<uidb64>/<token>/', views.activate_user, name='activate'),
    path('sign-up/',views.sign_up_user,name='sign-up'),
    # update profile urls
    # path("accounts/",include("django.contrib.auth.urls")),
    path('update_user/',views.update_user_profile,name='update_user'),
    path('update_password/',views.update_password,name='update_password'),
    # homepage urls
    path('home/',views.home_page,name='home'),
    # charts urls
    path('get_monthly_production_data/', views.get_monthly_production_data, name='get_monthly_production_data'),
    path('get_daily/',views.daily_chart,name='get_daily'),
    path('get_daily_production_data/', views.get_daily_production_data, name='get_daily_production_data'),
    path('get_hourly_production_data/', views.get_hourly_production_data, name='get_hourly_production_data'),
    # production urls
         # crqs production urls
    path('crqs-info/',views.production_crqs,name='crqs-info'),
    path('updaterecord/<int:pk>',views.update_record,name='updaterecord'),
    path('viewrecord/<int:pk>',views.view_record,name='viewrecord'),
    path('deleterecord/<int:pk>/', views.delete_record, name='deleterecord'),
    path('addrecord/',views.addrecord,name='addrecord'),
        
        #packing production urls 
    path('packing-info/',views.packing_info,name='packing-info'),
    path('pack-record/',views.packing_record,name='pack-record'),
    path('packviewrecord/<int:pk>/',views.packingviewrecord,name='packviewrecord'),
    path('packdeleterecord/<int:pk>/', views.packdelete_record, name='packdeleterecord'),
    path('packupdaterecord/<int:pk>',views.packupdate_record,name='packupdaterecord'),
    
        # mixing urls
    path('mixing/',views.production_mixing,name='mixing'),
    # vlemonkeproduct urls
    path('vlemonke/',views.production_vlemonke,name='vlemonke'),
    path('addrecordvlemonke/',views.addrecordvlemon,name='addrecordvlemonke'),
    path('viewrecordvlemonke/<int:pk>/',views.viewrecordvlemon,name='viewrecordvlemonke'),
    path('updaterecordvlemonke/<int:pk>/',views.updaterecordvlemon,name='updaterecordvlemonke'),
    path('deleterecordvlemonke/<int:pk>/',views.deleterecordvlemon,name='deleterecordvlemonke'),
    # vlavenderproduct
    path('addrecordvlavenderke/',views.addrecordvlavenderke,name='addrecordvlavenderke'),
    path('vlavenderke/',views.production_vlavenderke,name='vlavenderke'),
    path('viewrecordvlavenderke/<int:pk>/',views.viewrecordvlavenderke,name='viewrecordvlavenderke'),
    path('updaterecordvlavenderke/<int:pk>/',views.updaterecordvlavenderke,name='updaterecordvlavenderke'),
    path('deleterecordvlavenderke/<int:pk>/',views.deleterecordvlavender,name='deleterecordvlavenderke'),
    
]


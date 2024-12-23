from django.contrib import admin
from .models import *
from django.contrib.auth.models import User

# Register your models here.
admin.site.register(CRQSData)
admin.site.register(PackingData)
admin.site.register(VimLemonKe)
admin.site.register(VimLavenderKe)
admin.site.register(UserProfile)

# mix profile info and user info
class profileInline(admin.StackedInline):
    model=UserProfile
    
# extend user model
class UserAdmin(admin.ModelAdmin):
    model=User
    fields=['username','email','first_name','last_name']
    inlines=[profileInline]
    
# unregister the default user model/old way
admin.site.unregister(User)

# register the new user model/new way
admin.site.register(User,UserAdmin)
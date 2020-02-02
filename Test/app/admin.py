from django.contrib  import admin 
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from app.models import Profile, Email
from django.contrib.auth.models import User


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user','PathernalLastName','MathernalLastName','Cedula','Sexo', 'Edad')


@admin.register(Email)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('profile','Email')



class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'profiles'


class UserAdmin(BaseUserAdmin):

    inlines = (ProfileInline,)

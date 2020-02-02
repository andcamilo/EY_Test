from django.contrib  import admin 
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from app.models import Persona, Email
from django.contrib.auth.models import User


@admin.register(Persona)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('Name','PathernalLastName','MathernalLastName','Cedula','Sexo', 'Edad')


@admin.register(Email)
class EmailAdmin(admin.ModelAdmin):
    list_display = ('persona','Email','Orden')



class ProfileInline(admin.StackedInline):
    model = Persona
    can_delete = False
    verbose_name_plural = 'personas'


class UserAdmin(BaseUserAdmin):

    inlines = (ProfileInline,)

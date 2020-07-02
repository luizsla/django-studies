from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import Perfil

# Register your models here.
class PerfilInline(admin.StackedInline):
    model = Perfil
    can_delete = False
    verbose_name_plural = 'perfis'


class UserAdmin(BaseUserAdmin):
    inlines = (PerfilInline,) 

# registrando os novos modelos
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
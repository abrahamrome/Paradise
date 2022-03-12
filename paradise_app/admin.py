from django.contrib import admin
from .models import Perfil, Post, Album, Comentarios, Valoracion, Hashtag
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

admin.site.register(Perfil)
admin.site.register(Post)
admin.site.register(Album)
admin.site.register(Comentarios)
admin.site.register(Valoracion)
admin.site.register(Hashtag)
# Register your models here.

class UsuarioInline(admin.StackedInline):
	model = Perfil
	can_delete = False
	verbose_name_plural = 'usuario'

class UserAdmin(BaseUserAdmin):
	inlines = (UsuarioInline,)

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
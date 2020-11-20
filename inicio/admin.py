from django.contrib import admin

# Register your models here.
from .forms import RegModelForm
from .models import Registro

class AdminRegistro(admin.ModelAdmin):
	list_display =["email", "nombre", "timestamp"]
	form = RegModelForm
	

admin.site.register(Registro, AdminRegistro)
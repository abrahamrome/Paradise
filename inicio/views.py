from django.shortcuts import render
from .forms import RegForm, RegModelForm
from .models import Registro

# Create your views here.
def main(request):
		titulo = "Bienvenido %s" %(nombre)
	if request.user.is_authenticated:
		nombre = form.cleaned_data.get("nombre")
		titulo = "Bienvenido %s" %(nombre)
	form = RegModelForm(request.POST or None)
	context = {
		"formulario": form,
		"titulo": titulo, 
	}
	if form.is_valid():
		nombre = form.cleaned_data.get("nombre")
		form.save()

		context = {
			"titulo": "Gracias %s!" %(nombre)
		}

		
	return render(request, "inicio.html", context)
from django import forms

from .models import Registro

class RegModelForm(forms.ModelForm):
	class Meta:
		model = Registro
		fields = ["nombre","email"]

	def clean_email(self):
		email= self.cleaned_data.get("email")
		email_base, proveeder = email.split("@")
		dominio, extension = proveeder.split(".")
		if not extension == "com" or extension == "es":
			raise forms.ValidationError("Porfavor utiliza un email con la extension .com o .es")
		return email
	def clean_nombre(self):
		nombre = self.cleaned_data.get("nombre")
		return nombre

class RegForm(forms.Form):
	nombre = forms.CharField(max_length=100)
	email = forms.EmailField()
from django import forms
from paradise_app.models import Perfil, Post, Album, Comentarios, Valoracion
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
class PerfilForm(forms.ModelForm):
	class Meta:
		model = Perfil
		exclude =['usuario']



class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		exclude =['time', 'perfil']



class AlbumForm(forms.ModelForm):
	class Meta:
		model = Album
		exclude =['time', 'perfil']
		fields = ['publications', 'nombre']
	

	def __init__(self, *args, **kwargs):
		super(AlbumForm, self).__init__(*args, **kwargs)
		self.fields['publications'].queryset = Post.objects.filter(user=self.instance.user)


class ComentariosForm(forms.ModelForm):
	class Meta:
		model = Comentarios
		exclude =['perfil', 'post']

	


class ValoracionForm(forms.ModelForm):
	class Meta:
		model = Valoracion
		exclude =['perfil']

class RegistroPerfil(forms.ModelForm):

	class Meta:
		model = Perfil
		fields = ['biografia', 'foto']

class RegistroUser(UserCreationForm):

	class Meta:
		model = User
		fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
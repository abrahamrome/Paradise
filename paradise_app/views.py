from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from paradise_app.forms import PerfilForm, PostForm, AlbumForm, ComentariosForm, ValoracionForm
from .models import Album, Perfil, Comentarios, Valoracion, Post
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from paradise_app.forms import RegistroPerfil, RegistroUser
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.views.generic.base import TemplateResponseMixin
# Create your views here.

#Vista de index.html


	


def inicio (request):
	
	titulo = "Bienvenidos a Paradise"
	posts_todos = Post.objects.order_by('?')[:4]

	context = {
		'posts_todos': posts_todos
	}


	return render (request, "inicio.html", context)

#------------------------------------------------------------------------------
# Vistas genericas de modelos
class PerfilView(ListView):
	model = Perfil

class PostView(ListView):
	model = Post
	
	def get_queryset(self):
		url=self.request.get_full_path()
		urlcad=url.split('/')	
		queryset = super(PostView, self).get_queryset()
		return queryset.filter(perfil_id=urlcad[3])

class ComentariosView(LoginRequiredMixin, ListView):
	model = Comentarios
	def get_queryset(self):
		queryset = super(ComentariosView, self).get_queryset()
		return queryset.filter(post_id=Comentarios.pos)


class ValoracionView(LoginRequiredMixin, ListView):
	model = Valoracion

class AlbumView(LoginRequiredMixin,ListView):
	model = Album

#------------------------------------------------------------------------------
#Vistas detalles de modelos


class PerfilDetailView(DetailView):
	context_object_name = 'perfil'
	queryset = Perfil.objects.all()
	
	
	
	

class PostDetailView(DetailView):
	#model = Post
	#template_name = 'paradise_app/post_detail.html'
	context_object_name = 'post'
	queryset = Post.objects.all()
	



class AlbumDetailView(LoginRequiredMixin, DetailView):
	context_object_name = 'album'
	queryset = Album.objects.all()
	#a = Album.objects.get()
	

class ValoracionDetailView(LoginRequiredMixin, DetailView):
	context_object_name = 'valoracion'
	queryset = Valoracion.objects.all()

class ComentariosDetailView(LoginRequiredMixin, DetailView):
	context_object_name = 'comentarios'
	queryset = Comentarios.objects.all()

#------------------------------------------------------------------------------
# Vista de formulario para añadir nuevo

class PerfilCreate(LoginRequiredMixin, CreateView):
	model = Perfil
	form_class = PerfilForm
	success_url = reverse_lazy('Perfil')

class PostCreate(LoginRequiredMixin, CreateView):
	model = Post
	fields = ['descripcion', 'subir']
	success_url = reverse_lazy('inicio')
	def form_valid(self, form):
		form.instance.perfil = self.request.user.perfil
		#form.instance.subir = 'imagenes/45399.jpg'
		return super().form_valid(form)



class AlbumCreate(LoginRequiredMixin, CreateView):
	model = Album
	#form_class = AlbumForm
	fields = ['nombre', 'publications']
	success_url = reverse_lazy('Album')
	def form_valid(self, form):
		form.instance.perfil = self.request.user.perfil
		return super().form_valid(form)
	def get_form(self, form_class=None):
		if form_class is None:
			form_class = self.get_form_class()
			AlbumForm = form_class(**self.get_form_kwargs())
			AlbumForm['publications'].field.queryset = Post.objects.filter(perfil_id=self.request.user.perfil.pk)
			return AlbumForm


class ComentariosCreate(LoginRequiredMixin, CreateView):
	model = Comentarios
	fields = ['coment']
	#success_url = reverse_lazy('inicio')
	def form_valid(self, form):
		form.instance.perfil =self.request.user.perfil
		url=self.request.get_full_path()
		urlcad=url.split('/')
		objeto=Post.objects.get(pk=int(urlcad[3]))
		form.instance.post = objeto
		form.save()
		return redirect('Post-detalles', pk=urlcad[3])

	"""def form_valid(self, form):
        url=self.request.get_full_path()
        urlcad=url.split("/")
        objeto=Post.objects.get(pk=int(urlcad[3]))
        form.instance.post = objeto
        form.save()
        return redirect('Post-detalles', pk=urlcad[3])"""
	
	

class ValoracionCreate(LoginRequiredMixin, CreateView):
	model = Valoracion
	fields = ['foto', 'estrella']
	#form_class = ValoracionForm
	#success_url = reverse_lazy('Valoracion')
	def form_valid(self, form):
		form.instance.perfil =self.request.user.perfil
		url=self.request.get_full_path()
		urlcad=url.split('/')
		objeto=Post.objects.get(pk=int(urlcad[3]))
		form.instance.post = objeto
		form.save()
		return redirect('Post-detalles', pk=urlcad[3])



#------------------------------------------------------------------------------
# Vista de formulario para editar

class PerfilUpdateView(LoginRequiredMixin, UpdateView):
	model = Perfil
	form_class = PerfilForm
	success_url = reverse_lazy('inicio')
	
	def get_queryset(self):
		return super(PerfilUpdateView, self).get_queryset().filter(pk = self.request.user.perfil.pk)
	

		
		#form_class = PerfilForm
		


class PostUpdateView(LoginRequiredMixin, UpdateView):
	model = Post
	form_class = PostForm
	success_url = reverse_lazy('Post-detalles')
	def get_queryset(self):
				return super(PostUpdateView, self).get_queryset().filter(perfil_id= self.request.user.perfil.pk)
	#def user_valid(self):
		#if post.user = self.request.user

class AlbumUpdateView(LoginRequiredMixin, UpdateView):
	model = Album
	form_class = AlbumForm
	success_url = reverse_lazy('Album-detalles')
	def get_queryset(self):
		return super(AlbumUpdateView, self).get_queryset().filter(perfil_id = self.request.user.perfil.pk)

class ComentariosUpdateView(LoginRequiredMixin, UpdateView):
	model = Comentarios
	form_class = ComentariosForm
	success_url = reverse_lazy('Comentarios')
	def get_queryset(self):
		return super(ComentariosUpdateView, self).get_queryset().filter(perfil_id = self.request.user.perfil.pk)

class ValoracionUpdateView(LoginRequiredMixin, UpdateView):
	model = Valoracion
	form_class = ValoracionForm
	success_url = reverse_lazy('Valoracion')
	def get_queryset(self):
		return super(ValoracionUpdateView, self).get_queryset().filter(perfil_id = self.request.user.perfil.pk)
#------------------------------------------------------------------------------
# Vista para eliminar

class PerfilDeleteView(LoginRequiredMixin, DeleteView):
	model = Perfil
	success_url = reverse_lazy('Perfil')

class PostDeleteView(LoginRequiredMixin, DeleteView):

	model = Post
	success_url = reverse_lazy('Post')

class AlbumDeleteView(LoginRequiredMixin, DeleteView):
	model = Album
	success_url = reverse_lazy('Album')

class ComentariosDeleteView(LoginRequiredMixin, DeleteView):
	model = Comentarios
	success_url = reverse_lazy('Comentarios')

class ValoracionDeleteView(LoginRequiredMixin, DeleteView):
	model = Valoracion
	success_url = reverse_lazy('Valoracion')


#-------------------------------------------------

def register(request):
	if request.method == 'POST':
		form_user = RegistroUser(request.POST)
		form_perfil = RegistroPerfil(request.POST)
		if form_user.is_valid() and form_perfil.is_valid():
			usuario = form_user.save(commit=False)
			perfil = form_perfil.save(commit=False)
			perfil.usuario = usuario
			#email = form_user.cleaned.data.get('email')
			#user.email = email
			form_user.save()
			form_perfil.save()
			return redirect('inicio')
	else:
		form_user = RegistroUser()
		form_perfil = RegistroPerfil()
	context = { 'form_user' : form_user, 'form_perfil' : form_perfil }
	return render(request, 'registration/registro.html', context)


def search(request):
	if request.method == "POST":
		busqueda = request.POST['buscar']
		p = Perfil.objects.filter(username__contains=busqueda)

		return render(request, 'search/search_perfil.html', {'busqueda':busqueda, 'p':p})
	else:

		return render(request, 'search/search_perfil.html', {})



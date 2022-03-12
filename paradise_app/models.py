from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

ESTRELLAS = [(1,1),(2,2),(3,3),(4,4),(5,5)]

actual = timezone.now()

class Perfil(models.Model): 
	usuario = models.OneToOneField(User, on_delete=models.CASCADE)
	biografia = models.CharField(max_length=500)
	foto = models.ImageField(upload_to="imagenes", blank=True)
	

	def __str__(self):
		return self.usuario.username
	


class Post(models.Model):
	perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE)
	descripcion= models.CharField(max_length=256)
	time = models.DateTimeField(default=actual)
	#ubicacion2=PointField(null=True, blank=True)
	subir= models.ImageField(upload_to="imagenes")
	


	def __str__(self):

		return self.perfil.usuario.username

	
	
	
class Album(models.Model):
	nombre=models.CharField(max_length=50)
	time = models.DateTimeField(default=actual)
	perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE)
	publications = models.ManyToManyField(Post)
	

	def __str__(self):
		return self.nombre


class Comentarios(models.Model):
	coment = models.CharField(max_length=256)
	post= models.ForeignKey(Post, on_delete=models.CASCADE)
	perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE)

	def __str__(self):
		return self.perfil.usuario.username

class Valoracion(models.Model):
	foto=models.ForeignKey(Post, on_delete=models.CASCADE)
	estrella = models.IntegerField(choices=ESTRELLAS)
	perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE)

	def __str__(self):

		return self.perfil.usuario.username

class Hashtag(models.Model):
	post=models.ForeignKey(Post, on_delete=models.CASCADE)
	hashtag= models.CharField(max_length=100, blank=True)

	


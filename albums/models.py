from django.db import models

# Create your models here.
class Album(model.Model):
	propietario = models.ForeignKey('auth.User')
	descripcion = models.CharField(max_length=256, blank=True, null=True)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

class AlbumImage(models.Model):
	album = models.ForeignKey(Album, related_name='images')
	image = models.ImageField(upload_to='albums/images/')


	def __str__(self): 
		return str(self.image)

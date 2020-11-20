from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Registro(models.Model):
	nombre = models.CharField(max_length=100, blank=False, null=False)
	email =models.EmailField()
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

	def __str__(self): 
		return self.email
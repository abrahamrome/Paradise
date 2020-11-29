from django import forms
from .models import AlbumImage

class UploadImageForm(forms.ModelForm):


	class Meta:
		model = AlbumImage
		fields = ['album', 'image']
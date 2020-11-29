from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, RequestContext
from .forms import UploadImageForm

@login_required
def upload_image_view(request):
	if request.method == 'POST':
		form = UploadImageForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			mensaje = "Subida!"
	else:
		form = UploadImageForm()

	return render_to_response('albums/upload.html', locals(), context_instance=RequestContext(request))

def home_view(request):
	return render_to_response('base.html')

# Create your views here.

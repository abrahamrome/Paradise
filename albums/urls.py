from django.conf.urls import patterns, include, url


urlpatterns = patterns('albums.views',
    # Examples:
    url(r'^$', 'home_view', name='home_view'),
    url(r'^upload$', 'upload_image_view', name='upload_image_view'),

)

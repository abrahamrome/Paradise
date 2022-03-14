"""paradise URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.models import User
from paradise_app.models import Post, Perfil, Album, Comentarios
from rest_framework import routers, serializers, viewsets
from django.contrib.auth.decorators import permission_required



from paradise_app.views import PerfilView, AlbumView, PostView, ComentariosView, ValoracionView, ValoracionDetailView, ComentariosDetailView, inicio, AlbumDetailView, PostDetailView
from paradise_app.views import PerfilCreate, PostCreate, ComentariosCreate, ValoracionCreate, AlbumCreate, PerfilUpdateView, PostUpdateView, AlbumUpdateView, ComentariosUpdateView, ValoracionUpdateView
from paradise_app.views import PerfilDeleteView, PostDeleteView, AlbumDeleteView, ComentariosDeleteView, ValoracionDeleteView, inicio, register, search, PerfilDetailView

#-----------------API--------------------------------------

class PostSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Post
        fields = '__all__'

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PerfilSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Perfil
        fields = '__all__'

class PerfilViewSet(viewsets.ModelViewSet):
    queryset = Perfil.objects.all()
    serializer_class = PerfilSerializer


class ComentariosSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Comentarios
        fields = '__all__'

class ComentariosViewSet(viewsets.ModelViewSet):
    queryset = Comentarios.objects.all()
    serializer_class = ComentariosSerializer


class AlbumSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Album
        fields = '__all__'

class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


router = routers.DefaultRouter()
router.register(r'publicaciones', PostViewSet)
router.register(r'perfiles', PerfilViewSet)
router.register(r'albumes', AlbumViewSet)
router.register(r'comentarios', ComentariosViewSet)

#-----------------API--------------------------------------


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', inicio, name='inicio'),

    path('perfiles/', PerfilView.as_view(), name='Perfil'),
    path('perfil/<int:pk>/', PerfilDetailView.as_view(), name='Perfil-detalles'),
    path('perfil/<int:pk>/delete', PerfilDeleteView.as_view(), name='Perfil-delete'),
    path('perfil/<int:pk>/update', PerfilUpdateView.as_view(), name='Perfil-update'),
    path('perfiles/add', PerfilCreate.as_view(), name='Perfil-create'),

    path('comentario/<int:pk>/', ComentariosDetailView.as_view(), name='Comentarios-detalles'),
    path('comentario/<int:pk>/delete', ComentariosDeleteView.as_view(), name='Comentarios-delete'),
    path('comentario/<int:pk>/update', ComentariosUpdateView.as_view(), name='Comentarios-update'),
    path('comentarios/', ComentariosView.as_view(), name='Comentarios'),
    path('comentarios/add/<int:pk>/', ComentariosCreate.as_view(), name='Comentarios-create'),

    path('valoracion/<int:pk>/', ValoracionDetailView.as_view(), name='Valoracion-detalles'),
    path('valoracion/<int:pk>/detele', ValoracionDeleteView.as_view(), name='Valoracion-delete'),
    path('valoracion/<int:pk>/update', ValoracionUpdateView.as_view(), name='Valoracion-update'),
    path('valoraciones/', ValoracionView.as_view(), name='Valoracion'),
    path('valoraciones/add/<int:pk>/', ValoracionCreate.as_view(), name='Valoracion-create'),

    path('album/<int:pk>/', AlbumDetailView.as_view(), name='Album-detalles'),
    path('album/<int:pk>/detele', AlbumDeleteView.as_view(), name='Album-delete'),
    path('album/<int:pk>/update', AlbumUpdateView.as_view(), name='Album-update'),
    path('albumes/<int:pk>/', AlbumView.as_view(), name='Album'),
    path('albumes/add', AlbumCreate.as_view(), name='Album-create'),

    path('publicacion/<int:pk>/', PostDetailView.as_view(), name='Post-detalles'),
    path('publicacion/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
    path('publicacion/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('publicaciones/<int:pk>/', PostView.as_view(), name='Post'),
    path('publicaciones/add', PostCreate.as_view(), name='Post-create'),


    
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('change-password/', auth_views.PasswordChangeView.as_view(template_name='registration/password_reset_form.html'), name='password-reset'),
    path('accounts/logout', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),

    path('registro/', register, name='register'),
    path('search/', search, name='search'),

    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path(r'openid/', include('django_openid_auth.urls'), name='openid'),
    #path(r'auth/', include('googleauth.urls')),




] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



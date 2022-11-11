from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('busqueda', views.busqueda, name='busqueda'),
    path('detalle/<id_receta>', views.detalle, name='detalle'),
    path('mode', views.mode, name='mode'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
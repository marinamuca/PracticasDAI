from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('busqueda', views.busqueda, name='busqueda'),
    path('detalle/<id_receta>', views.detalle, name='detalle'),
    path('mode', views.mode, name='mode'),
    path('receta/new', views.receta_new, name='receta_new'),
    path('receta/edit/<id_receta>', views.receta_edit, name='receta_edit'),
    path('receta/delete/<id_receta>', views.receta_delete, name='receta_delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
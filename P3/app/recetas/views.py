from django.shortcuts import render, HttpResponse, redirect
from .models import Receta, Foto, Ingrediente
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def index(request):
    if not request.session.get('dark_mode'):
        request.session['dark_mode'] = False
    context = {
        'saludado': 'Pepito',
        'modo_oscuro': request.session['dark_mode']
    }
    return render(request, "base.html", context)

def busqueda(request):
    name = request.GET.get("search_input")
    recetas = Receta.objects.filter(nombre__icontains=name)
    context = {
        'recetas': recetas,
        'modo_oscuro': request.session['dark_mode']
    }

    return render(request, "busqueda.html", context)

def detalle(request, id_receta):
    receta = Receta.objects.filter(id=id_receta)
    imagenes = Foto.objects.filter(receta_id=id_receta)
    ingredientes = Ingrediente.objects.filter(receta_id=id_receta)
    context = {
        'receta': receta[0],
        'imagenes': imagenes,
        'ingredientes': ingredientes,
        'modo_oscuro': request.session['dark_mode']
    }
    return render(request, "detalle.html", context)

@csrf_exempt
def mode(request):
    if not request.session.__contains__('dark_mode'):
        request.session['dark_mode'] = False
    else:
        dark_mode = request.session['dark_mode'] 
        if dark_mode:
            request.session['dark_mode'] = False
        else:
            request.session['dark_mode'] = True

    return redirect(request.META['HTTP_REFERER'])
    
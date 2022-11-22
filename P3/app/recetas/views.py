from django.shortcuts import render, HttpResponse, redirect

from .forms import RecetaForm, IngredienteForm
from .models import Receta, Foto, Ingrediente
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
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
    
# ** P3.3

def receta_new(request):
    if request.method == "POST":
        formReceta = RecetaForm(request.POST)
        # formIngrediente = IngredienteForm(request.POST)
        if formReceta.is_valid():
            receta = formReceta.save()
            # ingrediente = formIngrediente.save(commit=False)
            # ingrediente.receta = receta
            # ingrediente.save()

        messages.add_message(request, messages.SUCCESS, 'Receta ' + receta.nombre + ' añadida correctamente.')
        return redirect('detalle', id_receta=receta.id)
    else:
        formReceta = RecetaForm
        formIngrediente = IngredienteForm
        context = {
            # 'receta': receta[0],
            # 'imagenes': imagenes,
            # 'ingredientes': ingredientes,
            'formReceta': formReceta,
            'formIngrediente': formIngrediente,
            'modo_oscuro': request.session['dark_mode']
        }
        return render(request, "addReceta.html", context)

def receta_edit(request, id_receta):
    receta = Receta.objects.get(id=id_receta)
    if request.method == 'POST':
        form = RecetaForm(request.POST, instance=receta)
        if form.is_valid():
            # update the existing `Band` in the database
            form.save()
            # redirect to the detail page of the `Band` we just updated
            messages.add_message(request, messages.SUCCESS, 'Receta ' + receta.nombre + ' editada correctamente.')
            return redirect('detalle', id_receta=receta.id)
        
    formReceta = RecetaForm(instance=receta)
    formIngrediente = IngredienteForm
    context = {
        'receta': receta,
        # 'imagenes': imagenes,
        # 'ingredientes': ingredientes,
        'formReceta': formReceta,
        'formIngrediente': formIngrediente,
        'modo_oscuro': request.session['dark_mode']
    }
    return render(request, "addReceta.html", context)

def receta_delete(request, id_receta):
    receta = Receta.objects.filter(id=id_receta)
    nombreReceta = receta[0].nombre
    receta.delete()

    messages.add_message(request, messages.SUCCESS, 'Receta ' + nombreReceta + ' eliminada correctamente.')
    return redirect(request.META['HTTP_REFERER'])
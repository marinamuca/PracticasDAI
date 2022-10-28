from django.contrib import admin
from .models import Receta, Foto, Ingrediente

# Register your models here.
admin.site.register(Receta)
admin.site.register(Foto)
admin.site.register(Ingrediente)

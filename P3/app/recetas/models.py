from enum import unique
from django.db import models
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
import os
import re

def validateFirstCapital(value):
  if not (re.match(pattern="([A-Z])", string=value)):
    raise ValidationError("¡El texto debe empezar por mayúscula!")
        
# Create your models here.
class Receta(models.Model):
  nombre       = models.CharField(max_length=200, unique=True, validators=[validateFirstCapital])
  preparacion  = models.TextField(max_length=5000, validators=[validateFirstCapital])
  
  def __str__(self):
    return self.nombre
  
class Ingrediente(models.Model):
  nombre        = models.CharField(max_length=100)
  cantidad      = models.PositiveSmallIntegerField()
  unidades      = models.CharField(max_length=10)
  receta        = models.ForeignKey(Receta, on_delete=models.CASCADE)

  def __str__(self):
    return self.nombre

class Foto(models.Model):
    receta        = models.ForeignKey(Receta, on_delete=models.CASCADE)
    foto          = models.FileField(upload_to='fotos')

    def __str__(self):
        return  os.path.basename(self.foto.name)
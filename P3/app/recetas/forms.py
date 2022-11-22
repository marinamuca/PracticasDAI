from django import forms
# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Submit
from .models import Receta, Ingrediente

class RecetaForm(forms.ModelForm):
     class Meta:
        model = Receta
        fields = ('__all__')

class IngredienteForm(forms.ModelForm):
     class Meta:
        model = Ingrediente
        fields = ('nombre', 'cantidad', 'unidades')

        # def __init__(self, *args, **kwargs):
        #     super().__init__(*args, **kwargs)
        #     self.helper = FormHelper()
        #     self.helper.form_method = 'post'
        #     self.helper.add_input(Submit('submit', 'Añadir'))
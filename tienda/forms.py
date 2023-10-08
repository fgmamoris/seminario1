from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre','apellido' , 'cantidad', 'precio', 'descripcion'] 
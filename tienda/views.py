from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Producto
from .forms import ProductoForm
from django.http import JsonResponse
import json

def post_list(request):
    return render(request, 'tienda/post_list.html', {})
def home(request):
    return render(request, 'home.html')
def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'lista_productos.html', {'productos': productos})
def crear_producto(request):
    print(request.body  )
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            form = ProductoForm(data)
            if form.is_valid():
                form.save()
                return JsonResponse({'message': 'Producto creado exitosamente.'}, status=200)
            else:
                return JsonResponse({'message': 'Error al crear el producto.'}, status=400)
        except Exception as e:
            return JsonResponse({'message': str(e)}, status=500)
    else:
        form = ProductoForm()
    return render(request, 'lista_productos.html', {'form': form})
def index(request):
    return render(request, 'index.html')



class ListaProductosView(TemplateView):
    template_name = 'productos_list.html'

    def get_context_data(self, **kwargs):
        context = {
            'productos': Producto.objects.all()
        }
        return context

class CrearProductoView(TemplateView):
    template_name = 'crear_producto.html'  
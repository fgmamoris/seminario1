from django.urls import path
from . import views
from .views import ListaProductosView, CrearProductoView
from .views import home  
from .views import index 


urlpatterns = [
   # path('', views.post_list, name='post_list'),
    #path('', home, name='home'), 
    path('', home, name='home'), 
     #path('lista_productos/', views.lista_productos, name='lista_productos'),
     path('lista_productos/', views.lista_productos, name='lista_productos'),
    path('crear_producto/', views.crear_producto, name='crear_producto'),
    path('crear/', CrearProductoView.as_view(), name='crear_producto'),
    path('eliminar_producto/<int:producto_id>/', views.eliminar_producto, name='eliminar_producto'),
    path('modificar_producto/<int:producto_id>/', views.modificar_producto, name='modificar_producto'),
    path('obtener_producto/<int:producto_id>/', views.obtener_producto, name='obtener_producto'),

]
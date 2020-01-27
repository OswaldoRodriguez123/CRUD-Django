from django.urls import path
from .views import ProductosListado, ProductoCrear, ProductoActualizar, ProductoEliminar

urlpatterns = [
    # La ruta 'index' en donde listamos todos los registros o productos de la Base de Datos
    path('', ProductosListado.as_view(template_name = "index.html"), name='index'),
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo producto o registro  
    path('create', ProductoCrear.as_view(template_name = "product.html"), name='create'),
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un producto o registro de la Base de Datos 
    path('update/<uuid:pk>', ProductoActualizar.as_view(template_name = "product.html"), name='actualizar'), 
    # La ruta 'eliminar' que usaremos para eliminar un producto o registro de la Base de Datos 
    path('delete/<uuid:pk>', ProductoEliminar.as_view(), name='eliminar'),    
]
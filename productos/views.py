from django.shortcuts import render
 
# Instanciamos las vistas genéricas de Django 
from django.views.generic import ListView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
 
# Instanciamos el modelo 'Productos' para poder usarlo en nuestras Vistas CRUD
from .models import Productos

# Nos sirve para redireccionar despues de una acción revertiendo patrones de expresiones regulares 
from django.urls import reverse
 
# Habilitamos el uso de mensajes en Django
from django.contrib import messages 
 
# Habilitamos los mensajes para class-based views 
from django.contrib.messages.views import SuccessMessageMixin 
 
# Habilitamos los formularios en Django
from django import forms

from django.db.models import Sum, F
from django.db.models.functions import Coalesce

class ProductoForm(forms.ModelForm):  
    class Meta:  
        model = Productos  
        fields = ['product_code']  

class ProductosListado(ListView): 
    model = Productos # Llamamos a la clase 'Productos' que se encuentra en nuestro archivo 'models.py'
    def get_queryset(self, **kwargs):
        return Productos.objects.all().annotate(
                product_stock=Sum(Coalesce('stocks__stock_cant',0))
            ).order_by('created_at')


class ProductoCrear(SuccessMessageMixin, CreateView): 
    model = Productos # Llamamos a la clase 'Productos' que se encuentra en nuestro archivo 'models.py'
    form = Productos # Definimos nuestro formulario con el nombre de la clase o modelo 'Productos'
    fields = ['product_code','product_name'] # Le decimos a Django que muestre todos los campos de la tabla 'productos' de nuestra Base de Datos 
    success_message = 'Producto Creado Correctamente !' # Mostramos este Mensaje luego de Crear un Productos
    
    def form_invalid(self, form):
        messages.warning(self.request, 'Este Codigo Ya Existe!')
        return self.render_to_response(
            self.get_context_data(request=self.request, form=form))
 
    # Redireccionamos a la página principal luego de crear un registro o producto
    def get_success_url(self):        
        return reverse('index') # Redireccionamos a la vista principal 'index'
        
class ProductoActualizar(SuccessMessageMixin, UpdateView): 
    model = Productos # Llamamos a la clase 'Productos' que se encuentra en nuestro archivo 'models.py' 
    form = Productos # Definimos nuestro formulario con el nombre de la clase o modelo 'Productos' 
    fields = ['product_code','product_name'] # Le decimos a Django que muestre todos los campos de la tabla 'productos' de nuestra Base de Datos 
    success_message = 'Producto Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Producto 

    def form_invalid(self, form):
        messages.warning(self.request, 'Este Codigo Ya Existe!')
        return self.render_to_response(
            self.get_context_data(request=self.request, form=form))
 
    # Redireccionamos a la página principal luego de actualizar un registro o producto
    def get_success_url(self):               
        return reverse('index') # Redireccionamos a la vista principal 'index'

class ProductoEliminar(SuccessMessageMixin, DeleteView): 
    model = Productos 
    form = Productos
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o producto
    def get_success_url(self): 
        success_message = 'Producto Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Producto 
        messages.success (self.request, (success_message))       
        return reverse('index') # Redireccionamos a la vista principal 'index'

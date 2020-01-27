from django.shortcuts import render
 
# Instanciamos las vistas genéricas de Django 
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, DeleteView
 
# Instanciamos el modelo 'Stocks' para poder usarlo en nuestras Vistas CRUD
from .models import Stocks

# Instanciamos el modelo 'Stocks' para poder usarlo en nuestras Vistas CRUD
from productos.models import Productos

# Instanciamos el modelo 'Stocks' para poder usarlo en nuestras Vistas CRUD
from .forms import StocksForm

# Nos sirve para redireccionar despues de una acción revertiendo patrones de expresiones regulares 
from django.urls import reverse
 
# Habilitamos el uso de mensajes en Django
from django.contrib import messages 
 
# Habilitamos los mensajes para class-based views 
from django.contrib.messages.views import SuccessMessageMixin 
 
# Habilitamos los formularios en Django
from django import forms

from django.db.models import Min
from django.db.models import Max
from django.db.models import Avg
import uuid

class StocksListado(ListView): 
    model = Stocks # Llamamos a la clase 'Stocks' que se encuentra en nuestro archivo 'models.py'
    def get_context_data(self, **kwargs):
        product_id = self.kwargs['product_id']
        context = super(StocksListado, self).get_context_data(**kwargs)
        filter_ = Stocks.objects.filter(product_id=product_id).order_by('created_at')
        context['StocksListado'] = filter_
        context['product_id'] = product_id
        return context
    def get_queryset(self, **kwargs):
        product_id = self.kwargs['product_id']
        return Stocks.objects.filter(product_id=product_id)

class StockCrear(SuccessMessageMixin, CreateView): 
    model = Stocks # Llamamos a la clase 'Stocks' que se encuentra en nuestro archivo 'models.py'
    form_class = StocksForm
    form = Stocks # Definimos nuestro formulario con el nombre de la clase o modelo 'Stocks'
    success_message = 'Stock Creado Correctamente !' # Mostramos este Mensaje luego de Crear un Stocks

    def get_context_data(self, **kwargs):
        product_id = self.kwargs['product_id']
        context = super(StockCrear, self).get_context_data(**kwargs)
        filter_ = Stocks.objects.filter(product_id=product_id)
        context['StockCrear'] = filter_
        context['product_id'] = product_id
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        if(int(self.request.POST['tipo']) == 1):
            self.object.stock_cant = abs(self.object.stock_cant)
            self.object.stock_value = self.object.stock_value / self.object.stock_cant
        else:
            self.object.stock_cant = -abs(self.object.stock_cant)
            self.object.stock_value = 0
        
        self.object.save()
        return super(StockCrear, self).form_valid(form)
 
    # Redireccionamos a la página principal luego de crear un registro o stock
    def get_success_url(self):    
        product_id = self.request.POST['product_id']
        if(int(self.request.POST['tipo']) == 1):
            stocks = Stocks.objects.filter(product_id=product_id).filter(stock_value__gte = 1)
            product_val_min = stocks.aggregate(Min('stock_value'))['stock_value__min']
            product_val_max = stocks.aggregate(Max('stock_value'))['stock_value__max']
            product_val_med = stocks.aggregate(Avg('stock_value'))['stock_value__avg']

            Productos.objects.filter(product_id=product_id).update(
                product_val_min=product_val_min,
                product_val_max=product_val_max,
                product_val_med=product_val_med,
                product_val_ult=int(self.request.POST['stock_value'])/abs(int(self.request.POST['stock_cant']))
            )
            
        return reverse('index_stock', kwargs={'product_id':product_id}) # Redireccionamos a la vista principal 'create'

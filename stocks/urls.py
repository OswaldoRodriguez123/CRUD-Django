from django.urls import path
from .views import StocksListado, StockCrear

urlpatterns = [
    # La ruta 'index' en donde listamos todos los registros o stocks de la Base de Datos
    path('<uuid:product_id>', StocksListado.as_view(template_name = "stock.html"), name='index_stock'),
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo stock o registro  
    path('create/<uuid:product_id>', StockCrear.as_view(template_name = "create.html"), name='create_stock'),   
]
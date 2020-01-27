# Create your models here.
from django.db import models
from django.utils import timezone
from productos.models import Productos
import uuid
 
# Creación de campos de la tabla 'stocks' 
class Stocks(models.Model):
    stock_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product_id = models.ForeignKey(Productos, on_delete=models.CASCADE)
    stock_cant = models.IntegerField(verbose_name="Cantidad")
    stock_value = models.FloatField(verbose_name="Valor",default=0)
    stock_vence = models.DateField(verbose_name="Fecha de Vencimiento")
    stock_serie = models.CharField(max_length=255,verbose_name="Numero de Lote")
    created_at = models.DateTimeField(auto_now_add=True,verbose_name="Fecha de Creacion")
    updated_at = models.DateTimeField(auto_now=True,verbose_name="Fecha de Actualizacion")
 
    class Meta:
        db_table = 'stocks' # Le doy de nombre 'stocks' a la tabla en la Base de Datos
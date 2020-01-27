# Create your models here.
from django.db import models
from django.utils import timezone
import uuid
 
# Creación de campos de la tabla 'productos' 
class Productos(models.Model):
    product_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product_code = models.CharField(max_length=50,verbose_name="Codigo", unique=True)
    product_name = models.CharField(max_length=255,verbose_name="Nombre")
    product_val_min = models.FloatField(default=0,verbose_name="Precio Minimo")
    product_val_med = models.FloatField(default=0,verbose_name="Precio Promedio")
    product_val_max = models.FloatField(default=0,verbose_name="Precio Maximo")
    product_val_ult = models.FloatField(default=0,verbose_name="Precio Ultimo")
    created_at = models.DateTimeField(auto_now_add=True,verbose_name="Fecha de Creacion")
    updated_at = models.DateTimeField(auto_now=True,verbose_name="Fecha de Actualizacion")
 
    class Meta:
        db_table = 'productos' # Le doy de nombre 'productos' a la tabla en la Base de Datos
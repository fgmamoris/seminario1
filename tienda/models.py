from django.db import models

class Producto(models.Model):
    id = models.IntegerField(primary_key = True)
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad = models.IntegerField(default=0)
    sku = models.IntegerField(default=0)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre
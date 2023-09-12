from django.core.management.base import BaseCommand
from tienda.models import Producto

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        # Crea productos y guárdalos en la base de datos
        Producto.objects.create(
            nombre='Producto 1',
            precio=10.00,
            cantidad=5,
            sku=1001,
            descripcion='Descripción del producto 1'
        )

        Producto.objects.create(
            nombre='Producto 2',
            precio=15.00,
            cantidad=8,
            sku=1002,
            descripcion='Descripción del producto 2'
        )

        self.stdout.write(self.style.SUCCESS('Datos insertados exitosamente.'))
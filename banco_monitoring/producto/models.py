from django.db import models

from solicitud.models import Solicitud
class Producto(models.Model):
    tipo_producto = models.CharField(max_length=50)
    cupo = models.EmailField(max_length=100)
    solicitud = models.ForeignKey(Solicitud, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.name)
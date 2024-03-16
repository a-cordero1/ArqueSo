from django.db import models

class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    salario = models.FloatField()
    correo = models.EmailField(max_length=255)
    numeroTelefonico = models.CharField(max_length=20)

    def __str__(self):
        return '{}'.format(self.nombre)

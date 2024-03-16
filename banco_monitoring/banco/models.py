from django.db import models

class Banco(models.Model):
    nombre = models.CharField(max_length=100)
    sede = models.CharField(max_length=100)

    def __str__(self):
        return '{}'.format(self.nombre)

from django.db import models

class Documento(models.Model):
    nombre = models.CharField(max_length=100)
    
    def __str__(self):
        return '{}'.format(self.nombre)
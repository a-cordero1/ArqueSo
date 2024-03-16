from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    correo = models.EmailField(max_length=255)
    numeroTelefonico = models.CharField(max_length=20)

    def __str__(self):
        return '{}'.format(self.nombre)

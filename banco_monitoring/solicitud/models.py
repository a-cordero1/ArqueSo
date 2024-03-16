from django.db import models

from banco.models import Banco
from cliente.models import Cliente
from documento.models import Documento
from empleado.models import Empleado
from codeudor.models import Codeudor

class Solicitud(models.Model):
    banco = models.ForeignKey(Banco, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    documento = models.ForeignKey(Documento, on_delete=models.CASCADE)
    empleados = models.ManyToManyField(Empleado)
    codeudor = models.OneToOneField(Codeudor, on_delete=models.CASCADE, primary_key=True)
    
    tipo = models.CharField(max_length=100)
    fecha = models.DateField()
    
    def __str__(self):
        return '{} - {}'.format(self.tipo, self.fecha)
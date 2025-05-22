from django.db import models
from Aplicaciones.Empleado.models import Empleado
from Aplicaciones.Vinedo.models import Vinedo
# Create your models here.
class Muestreo(models.Model):
    fecha = models.DateField()
    resultados = models.TextField()
    analista = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    vinedo = models.ForeignKey(Vinedo, on_delete=models.CASCADE)
from django.db import models

# Create your models here.
class Vinedo(models.Model):
    id = models.AutoField(primary_key=True)
    ubicacion = models.TextField()
    hectareas = models.IntegerField()
    variedad_uva = models.CharField(max_length=100) 
    anio_plantacion = models.IntegerField() 

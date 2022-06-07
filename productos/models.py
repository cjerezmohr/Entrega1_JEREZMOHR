from django.db import models

# Create your models here.

class Desktop_notebook(models.Model):
    marca = models.CharField(max_length=30)
    modelo = models.CharField(max_length=30)
    disco =  models.CharField(max_length=20)
    memoria = models.CharField(max_length=20)
    precio = models.FloatField()
    activo = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Equipo'
        verbose_name_plural = 'Equipos'

class Periferico(models.Model):
    tipo = models.CharField(max_length=50)
    marca = models.CharField(max_length=30)
    modelo =  models.CharField(max_length=30)
    precio =  models.FloatField()
    activo = models.BooleanField(default=True)

class Monitor(models.Model):
    tipo = models.CharField(max_length=10)
    marca = models.CharField(max_length=30)
    modelo =  models.CharField(max_length=30)
    resolucion = models.CharField(max_length=30)
    conexion =  models.CharField(max_length=30)
    precio =  models.FloatField()
    activo = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Monitor'
        verbose_name_plural = 'Monitores'

from django.db import models


# Create your models here.


class Jugador(models.Model):
    nombre = models.CharField(max_length=30)
    seleccion = models.CharField(max_length=30)
    #posicion = models.CharField(max_lenght=20) #a partir de acá para abajo, no me lo toma.
    #clubactual = models.CharField(max_lenght=20)
    dorsal = models.IntegerField()

#class Selecciones(models.Model):
    #seleccion = models.CharField(max_lenght=30)
    #banderacolor = models.CharField(max_lenght=20)


#class Estadios(models.Model):
    #nombreestadio = models.CharField(max_lenght=20)
    #ubicacion = models.CharField(max_lenght=20)


#class Partidos8vos(models.Model):
    #versus = models.CharField(max_lenght=60)
    #fecha = models.DateField()
    #horario = models.TimeField()
    #ganador = models.CharField(max_lenght=30)

  









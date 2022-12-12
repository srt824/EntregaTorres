from django.db import models


# Create your models here.


class Jugador(models.Model):
    nombre = models.CharField(max_length=30, null=True, blank=True)
    seleccion = models.CharField(max_length=30, null=True, blank=True)
    posicion = models.CharField(max_length=20, null=True, blank=True) 
    clubactual = models.CharField(max_length=30, null=True)
    dorsal = models.IntegerField()

class Selecciones(models.Model):
    seleccion = models.CharField(max_length=30, null=True, blank=True)
    banderacolor = models.CharField(max_length=30, null=True, blank=True)


class Grupos(models.Model):
    GrupoA = models.CharField(max_length=40, null=True, blank=True)
    GrupoB = models.CharField(max_length=40, null=True, blank=True)
    GrupoC = models.CharField(max_length=40, null=True, blank=True)
    GrupoD = models.CharField(max_length=40, null=True, blank=True)
    GrupoE = models.CharField(max_length=40, null=True, blank=True)
    GrupoF = models.CharField(max_length=40, null=True, blank=True)
    GrupoG = models.CharField(max_length=40, null=True, blank=True)
    GrupoH = models.CharField(max_length=40, null=True, blank=True)


class Estadios(models.Model):
    nombreestadio = models.CharField(max_length=20, null=True, blank=True)
    ubicacion = models.CharField(max_length=20,null=True, blank=True)


class Fase_grupos(models.Model):
    grupo = models.CharField(max_length=20, null=True, blank=True)
    versus = models.CharField(max_length=60, null=True, blank=True)
    estadio = models.CharField(max_length=20, null=True, blank=True)
    arbitro = models.CharField(max_length=30, null=True, blank=True)
    fecha = models.DateField()
    horario = models.TimeField()
    resultado = models.CharField(max_length=60, null=True, blank=True)
    ganador = models.CharField(max_length=30, null=True, blank=True)



class Partidos_octavos(models.Model):
    versus = models.CharField(max_length=60, null=True, blank=True)
    estadio = models.CharField(max_length=20, null=True, blank=True)
    arbitro = models.CharField(max_length=30, null=True, blank=True)
    fecha = models.DateField()
    horario = models.TimeField()
    resultado = models.CharField(max_length=60, null=True, blank=True)
    ganador = models.CharField(max_length=30, null=True, blank=True)


class Partidos_cuartos(models.Model):
    versus = models.CharField(max_length=60, null=True, blank=True)
    estadio = models.CharField(max_length=20, null=True, blank=True)
    arbitro = models.CharField(max_length=30, null=True, blank=True)
    fecha = models.DateField()
    horario = models.TimeField()
    resultado = models.CharField(max_length=60, null=True, blank=True)
    ganador = models.CharField(max_length=30, null=True, blank=True)


class Partidos_semis(models.Model):
    versus = models.CharField(max_length=60, null=True, blank=True)
    fecha = models.DateField()
    estadio = models.CharField(max_length=20, null=True, blank=True)
    arbitro = models.CharField(max_length=30, null=True, blank=True)
    horario = models.TimeField()
    resultado = models.CharField(max_length=60, null=True, blank=True)
    ganador = models.CharField(max_length=30, null=True, blank=True)


class La_final(models.Model):
    versus = models.CharField(max_length=60, null=True, blank=True)
    fecha = models.DateField()
    estadio = models.CharField(max_length=20, null=True, blank=True)
    arbitro = models.CharField(max_length=30, null=True, blank=True)
    horario = models.TimeField()
    resultado = models.CharField(max_length=60, null=True, blank=True)
    campeon = models.CharField(max_length=30, null=True, blank=True)


class Arbitros(models.Model):
    nombre = models.CharField(max_length=30, null=True, blank=True)
    nacionalidad = models.CharField(max_length=20, null=True, blank=True)
    

  









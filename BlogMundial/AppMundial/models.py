from django.db import models



# Create your models here.


class Jugador(models.Model):
    nombre = models.CharField(max_length=30, null=True, blank=True)
    edad = models.IntegerField(null=True, blank=True)
    seleccion = models.CharField(max_length=30, null=True, blank=True)
    posicion = models.CharField(max_length=20, null=True, blank=True) 
    clubactual = models.CharField(max_length=30, null=True)
    dorsal = models.IntegerField()

    def __str__(self):
        return self.nombre

class Selecciones(models.Model):
    nombre = models.CharField(max_length=30, null=True, blank=True)
    bandera_color = models.CharField(max_length=30, null=True, blank=True)
    director_tecnico = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return self.nombre


class Grupos(models.Model):
    categoria = models.CharField(max_length=10, null=True, blank=True)
    paises = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.categoria


class Estadios(models.Model):
    nombre_estadio = models.CharField(max_length=30, null=True, blank=True)
    ubicacion = models.CharField(max_length=20,null=True, blank=True)
    capacidad = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.nombre_estadio


class Fase_grupos(models.Model):
    grupo = models.CharField(max_length=20, null=True, blank=True)
    partido = models.CharField(max_length=60, null=True, blank=True)
    estadio = models.CharField(max_length=20, null=True, blank=True)
    arbitro = models.CharField(max_length=30, null=True, blank=True)
    fecha = models.DateField()
    horario = models.TimeField()
    resultado = models.CharField(max_length=60, null=True, blank=True)
    ganador = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return self.partido


class Partidos_octavos(models.Model):
    versus = models.CharField(max_length=60, null=True, blank=True)
    estadio = models.CharField(max_length=20, null=True, blank=True)
    arbitro = models.CharField(max_length=30, null=True, blank=True)
    fecha = models.DateField()
    horario = models.TimeField()
    resultado = models.CharField(max_length=60, null=True, blank=True)
    ganador = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return self.versus


class Partidos_cuartos(models.Model):
    versus = models.CharField(max_length=60, null=True, blank=True)
    estadio = models.CharField(max_length=20, null=True, blank=True)
    arbitro = models.CharField(max_length=30, null=True, blank=True)
    fecha = models.DateField()
    horario = models.TimeField()
    resultado = models.CharField(max_length=60, null=True, blank=True)
    ganador = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return self.versus


class Partidos_semis(models.Model):
    versus = models.CharField(max_length=60, null=True, blank=True)
    fecha = models.DateField()
    estadio = models.CharField(max_length=20, null=True, blank=True)
    arbitro = models.CharField(max_length=30, null=True, blank=True)
    horario = models.TimeField()
    resultado = models.CharField(max_length=60, null=True, blank=True)
    ganador = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return self.versus


class Tercer_puesto(models.Model):
    versus = models.CharField(max_length=60, null=True, blank=True)
    fecha = models.DateField()
    estadio = models.CharField(max_length=20, null=True, blank=True)
    arbitro = models.CharField(max_length=30, null=True, blank=True)
    horario = models.TimeField()
    resultado = models.CharField(max_length=60, null=True, blank=True)
    ganador = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return self.versus


class La_final(models.Model):
    versus = models.CharField(max_length=60, null=True, blank=True)
    fecha = models.DateField()
    estadio = models.CharField(max_length=20, null=True, blank=True)
    arbitro = models.CharField(max_length=30, null=True, blank=True)
    horario = models.TimeField()
    resultado = models.CharField(max_length=60, null=True, blank=True)
    campeon = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return self.versus


class Arbitros(models.Model):
    nombre = models.CharField(max_length=30, null=True, blank=True)
    edad = models.IntegerField(null=True, blank=True)
    nacionalidad = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.nombre









from django.shortcuts import render
from django.http import HttpResponse
from AppMundial.models import Jugador, Selecciones, Grupos
from django.core import serializers
from AppMundial.forms import JugadorFormulario

# Create your views here.

def mostrargrupos(request):
    grupos_datos = Grupos.objects.all()
    return render(request, "AppMundial/resultado_grupos.html", {"grupos_datos" : grupos_datos})


def buscando2(request):
    seleccion = request.GET['seleccion']
    seleccion_datos = Selecciones.objects.filter(seleccion=seleccion).last()
    return render(request, "AppMundial/resultadoSeleccion.html", {"seleccion_datos" : seleccion_datos})


def buscarseleccion(request):
    return render(request, "AppMundial/selecciones_busqueda.html")


def buscando(request):
    jugador = request.GET['nombre']
    jugador_datos = Jugador.objects.filter(nombre=jugador).last()
    return render(request, "AppMundial/resultadoJugador.html", {"jugador_datos" : jugador_datos})


def buscarjugador(request):
    return render(request, "AppMundial/jugadores_busqueda.html")


def inicio(request):
    return render(request,'AppMundial/inicio.html')


def jugadores(request):
    if request.method == "POST":
        miFormulario = JugadorFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            print(informacion)

            jugadores = Jugador(nombre=informacion["nombre"], seleccion=informacion["seleccion"], dorsal=informacion["dorsal"], posicion=informacion["posicion"], clubactual=informacion["clubactual"])
            jugadores.save()
            return render(request, "AppMundial/inicio.html")

    else:
        miFormulario = JugadorFormulario

    return render(request, "AppMundial/jugadores.html", {"miFormulario": miFormulario})

    
def jugadorapi(request):
    jugadores_all = Jugador.objects.all()
    return HttpResponse(serializers.serialize('json', jugadores_all))







from django.shortcuts import render
from django.http import HttpResponse
from AppMundial.models import Jugador#, #partidos8vos
from django.core import serializers
from AppMundial.forms import JugadorFormulario

# Create your views here.

def buscar(request):
    nombre=request.GET['nombre']
    return HttpResponse(f'Buscando al jugador {request}')


def buscarjugador(request):
    return render(request,'AppMundial/jugadoresBusqueda.html')


def inicio(request):
    return render(request,'AppMundial/inicio.html')


def jugadores(request):
    if request.method == "POST":
        miFormulario = JugadorFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            print(informacion)

            jugadores = Jugador(nombre=informacion["nombre"], seleccion=informacion["seleccion"], dorsal=informacion["dorsal"])
            jugadores.save()
            return render(request, "AppMundial/inicio.html")

    else:
        miFormulario = JugadorFormulario

    return render(request, "AppMundial/jugadores.html", {"miFormulario": miFormulario})

    
def jugadorapi(request):
    jugadores_all = Jugador.objects.all()
    return HttpResponse(serializers.serialize('json', jugadores_all))


def partidos(request):
    partidos_all = Partidos8vos.objects.all()
    return HttpResponse(serializers.serialize('json', partidos8vos))

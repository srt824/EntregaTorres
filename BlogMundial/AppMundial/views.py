from django.shortcuts import render
from django.http import HttpResponse
from AppMundial.models import Jugador, Selecciones, Grupos, Fase_grupos
from django.core import serializers
from AppMundial.forms import JugadorFormulario

# Create your views here.

def mostrargrupos(request):
    grupos_datos = Grupos.objects.all()
    return render(request, "AppMundial/resultado_grupos.html", {"grupos_datos" : grupos_datos})


def buscandopartido(request):
    partido = request.GET['partido']
    fase_grupos_datos = Fase_grupos.objects.filter(partido=partido).last()
    return render(request, "AppMundial/resultadoFase.html", {"fase_grupos_datos" : fase_grupos_datos})


def buscarpartido(request):
    return render(request, "AppMundial/fase_grupos_busqueda.html")


def buscarseleccion(request):
    return render(request, "AppMundial/selecciones_busqueda.html")


def buscando2(request):
    nombre = request.GET['selecciones']
    seleccion_datos = Selecciones.objects.filter(nombre=nombre).last()
    return render(request, "AppMundial/resultadoSeleccion.html", {"seleccion_datos" : seleccion_datos})


def buscando(request):
    nombre = request.GET['nombre']
    jugador_datos = Jugador.objects.filter(nombre=nombre).last()
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

    
def leer_jugadores(request):
    jugadores_all = Jugador.objects.all()
    return HttpResponse(serializers.serialize('json', jugadores_all))


def crear_jugador(request):
    jugador = Jugador(nombre = 'Lionel Messi', edad = 35, seleccion = 'Argentina', posicion = 'delantero', clubactual = 'Paris Saint-Germain', dorsal = 10, )
    jugador.save()
    return HttpResponse(f'El jugador {jugador.nombre} ha sido agregado')


def editar_jugador(request):
    nombre_consulta = 'Lionel Messi'
    Jugador.objects.filter(nombre=nombre_consulta).update(nombre='NombrenuevoLionelMessi')
    return HttpResponse(f'El jugador {nombre_consulta} ha sido actualizado')


def eliminar_jugador(request):
    nombre_nuevo = 'NombrenuevoLionelMessi'
    jugador = Jugador.objects.get(nombre=nombre_nuevo)
    jugador.delete()
    return HttpResponse(f'El jugador {nombre_nuevo} ha sido eliminado')

# Vistas basadas en Clases

from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# CRUD

class JugadorList(ListView):
    model = Jugador
    template_name = 'AppMundial/jugador_list.html'


class JugadorCreate(CreateView):
    model = Jugador
    fields = '__all__'
    success_url = '/AppMundial/jugador/list/'


class JugadorEdit(UpdateView):
    model = Jugador
    fields = '__all__'
    success_url = '/AppMundial/jugador/list/'

from django.views.generic.detail import DetailView


class JugadorDetail(DetailView):
    model = Jugador
    template_name = 'AppMundial/jugador_detail.html'


class JugadorDelete(DeleteView):
    model = Jugador
    #fields = '__all__'
    success_url = '/AppMundial/jugador/list/'


class SeleccionesList(ListView):
    model = Selecciones
    template_name = 'AppMundial/seleccion_list.html'


class SeleccionesCreate(CreateView):
    model = Selecciones
    fields = '__all__'
    success_url = '/AppMundial/seleccion/lists/'


class SeleccionesEdit(UpdateView):
    model = Selecciones
    fields = '__all__'
    success_url = '/AppMundial/seleccion/lists/'


class SeleccionesDetail(DetailView):
    model = Selecciones
    template_name = 'AppMundial/seleccion_detail.html'


class SeleccionesDelete(DeleteView):
    model = Selecciones
    #fields = '__all__'
    success_url = '/AppMundial/selecciones/lists/'


class Fase_gruposList(ListView):
    model = Fase_grupos
    template_name = '/AppMundial/fase_grupos_list.html'


class Fase_gruposCreate(CreateView):
    model = Fase_grupos
    fields = '__all__'
    success_url = '/AppMundial/fasegrupos/listfg/'


class Fase_gruposEdit(UpdateView):
    model = Fase_grupos
    fields = '__all__'
    success_url = '/AppMundial/fasegrupos/listfg/'


class Fase_gruposDetail(DetailView):
    model = Fase_grupos
    template_name = 'AppMundial/fase_grupos_detail.html'


class Fase_gruposDelete(DeleteView):
    model = Fase_grupos
    #fields = '__all__'
    success_url = '/AppMundial/fasegrupos/listfg/'







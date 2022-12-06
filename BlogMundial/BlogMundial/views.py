from django.http import HttpResponse
import datetime
from django.template import Template, Context
import os.path
from django.template import loader


PROJECT_PATH = os.path.realpath(os.path.dirname(__file__))
TEMPLATES_PATH = os.path.join(PROJECT_PATH, 'templates/')


def inicio(request):
    return HttpResponse("Bienvenidos al Blog del Mundial")


def dia_hoy(request):
    dia = datetime.datetime.now()
    
    documento = f'Fecha de hoy: <br> {dia}'

    return HttpResponse(documento)


def probandoTemplate(self):

    #miHtml = open("C:/Users/Antonelaa/Desktop/EntregaTorres/BlogMundial/BlogMundial/templates/template1.html")

    #plantilla = Template(miHtml.read())

    #miHtml.close()

    #miContexto = Context()

    #miDocumento = plantilla.render(miContexto)

    plantilla = loader.get_template('template1.html')

    return HttpResponse(miDocumento)

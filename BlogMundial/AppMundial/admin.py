from django.contrib import admin

from AppMundial.models import Jugador, Selecciones, Grupos, Estadios, Fase_grupos, Partidos_octavos, Partidos_cuartos, Partidos_semis, Tercer_puesto, La_final, Arbitros

class JugadorAdmin(admin.ModelAdmin):
    search_fields=("nombre", "seleccion")

admin.site.register(Jugador, JugadorAdmin)
admin.site.register(Selecciones)
admin.site.register(Grupos)
admin.site.register(Estadios)
admin.site.register(Fase_grupos)
admin.site.register(Partidos_octavos)
admin.site.register(Partidos_cuartos)
admin.site.register(Partidos_semis)
admin.site.register(Tercer_puesto)
admin.site.register(La_final)
admin.site.register(Arbitros)

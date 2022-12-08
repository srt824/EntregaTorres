from django.urls import path
from AppMundial import views


urlpatterns = [
    path('', views.inicio, name='Inicio'),
    path('jugadores/', views.jugadores, name='Jugador'),
    path('Partidos_octavos/', views.partidos, name='partidos'),
    path('jugadoresApi/', views.jugadorapi),
    path('busquedaJugador/', views.buscarjugador),
    path('buscar/', views.buscar)
    
]
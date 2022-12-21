from django.urls import path
from AppMundial import views


urlpatterns = [
    path('', views.inicio, name='Inicio'),
    path('jugadores/', views.jugadores, name='Jugador'),
    path('jugadoresApi/', views.jugadorapi),
    path('AppMundial/busquedaJugador/', views.buscarjugador, name='Buscar'),
    path('AppMundial/buscando/', views.buscando),
    path('AppMundial/busquedaSeleccion/', views.buscarseleccion, name='buscandoSeleccion'),
    path('AppMundial/buscandoSeleccion/', views.buscando2),
    path('AppMundial/grupos/', views.mostrargrupos, name='grupos'),
    




]
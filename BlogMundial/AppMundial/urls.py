from django.urls import path
from AppMundial import views


urlpatterns = [
    path('', views.inicio, name='Inicio'),
    path('jugadores/', views.jugadores, name='Jugador'),
    path('jugadoresApi/', views.jugadorapi),
    path('AppMundial/busquedaJugador/', views.buscarjugador, name='Buscar'),
    path('AppMundial/buscando/', views.buscando),
    path('AppMundial/busquedaSeleccion/', views.buscarseleccion, name='buscandoS'),
    path('AppMundial/buscandoS/', views.buscando2),
    path('AppMundial/buscargr/', views.buscargrupo),
    path('AppMundial/grupos/', views.mostrargrupos),
    




]
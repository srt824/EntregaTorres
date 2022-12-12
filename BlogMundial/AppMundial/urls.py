from django.urls import path
from AppMundial import views


urlpatterns = [
    path('', views.inicio, name='Inicio'),
    path('jugadores/', views.jugadores, name='Jugador'),
    path('jugadoresApi/', views.jugadorapi),
    path('AppMundial/busquedaJugador/', views.buscarjugador),
    path('AppMundial/buscando/', views.buscando),

    
]
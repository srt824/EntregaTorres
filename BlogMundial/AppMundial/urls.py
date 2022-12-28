from django.urls import path
from AppMundial import views


urlpatterns = [
    path('', views.inicio, name='Inicio'),
    path('AppMundial/busquedaJugador/', views.buscarjugador, name='buscarJ'),
    path('AppMundial/buscando/', views.buscando),
    path('AppMundial/busquedaSeleccion/', views.buscarseleccion, name='buscarS'),
    path('AppMundial/buscandoSeleccion/', views.buscando2),
    path('AppMundial/busquedapartido/', views.buscarpartido, name='buscarP'),
    path('AppMundial/buscandopartido/', views.buscandopartido),
    path('AppMundial/grupos/', views.mostrargrupos, name='grupos'),
    path('AppMundial/jugador/list/', views.JugadorList.as_view(), name='List'),
    path('jugador/create/', views.JugadorCreate.as_view(), name='New'),
    path('jugador/edit/<pk>', views.JugadorEdit.as_view(), name='Edit'),
    path('jugador/detail/<pk>', views.JugadorDetail.as_view(), name='Detail'),
    path('jugador/delete/<pk>', views.JugadorDelete.as_view(), name='Delete'),
    path('AppMundial/selecciones/list', views.SeleccionesList.as_view(), name='Lists'),
    path('selecciones/create/', views.SeleccionesCreate.as_view(), name='News'),
    path('selecciones/edit/<pk>', views.SeleccionesEdit.as_view(), name='Edits'),
    path('selecciones/detail/<pk>', views.SeleccionesDetail.as_view(), name='Details'),
    path('selecciones/delete/<pk>', views.SeleccionesDelete.as_view(), name='Deletes'),
    path('AppMundial/fasegrupos/list', views.Fase_gruposList.as_view(), name='Listfg'),
    path('fasegrupos/create/', views.Fase_gruposCreate.as_view(), name='Newfg'),
    path('fasegrupos/edit/<pk>', views.Fase_gruposEdit.as_view(), name='Editfg'),
    path('fasegrupos/detail/<pk>', views.Fase_gruposDetail.as_view(), name='Detailfg'),
    path('fasegrupos/delete/<pk>', views.Fase_gruposDelete.as_view(), name='Deletefg'),

    

    




]
from django.urls import path
from AppCoder import views

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('CargaEquipo', views.CargaEquipo, name="CargaEquipo"),
    path('CargaJugador', views.CargaJugador, name="CargaJugador"),
    path('BusquedaJugador', views.busquedaJugador, name = 'BusquedaJugador'),
    path('BusquedaEquipo', views.BusquedaEquipos, name = 'BusquedaEquipo'),
    path('buscarJugador/', views.BuscarJugador),
    path('BuscarEquipo/', views.BuscarEquipo)
]


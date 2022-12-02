from django.urls import path
from AppCoder import views

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('Equipo', views.Equipos, name="Equipo"),
    path('Jugador', views.Jugadores, name="Jugador"),
    path('BusquedaJugador', views.busquedaJugador, name = 'BusquedaJugador'),
    path('buscar/', views.buscar)
]


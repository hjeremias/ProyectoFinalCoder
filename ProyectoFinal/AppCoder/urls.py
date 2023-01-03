from django.urls import path
from AppCoder import views

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('CargaEquipo', views.CargaEquipo, name="CargaEquipo"),
    path('CargaJugador', views.CargaJugador, name="CargaJugador"),
    path('BusquedaJugador', views.busquedaJugador, name = 'BusquedaJugador'),
    path('BusquedaEquipo', views.BusquedaEquipos, name = 'BusquedaEquipo'),
    path('buscarJugador/', views.BuscarJugador),
    path('BuscarEquipo/', views.BuscarEquipo),
    
    ######      CBV       #######

    path('jugador/list', views.JugadorList.as_view(), name = 'ListJug'),
    path(r'^(?P<pk>\d+)$', views.JugadorDetalle.as_view(), name = 'DetalleJug'),
    path(r'^nuevo$', views.JugadorCreate.as_view(), name = 'CreateJug'),
    path(r'^editar/(?P<pk>\d+)$', views.JugadorUpdate.as_view(), name = 'UpdateJug'),
    path(r'^borrar/(?P<pk>\d+)$', views.JugadorDelete.as_view(), name = 'DeleteJug'),

    path('equipo/list', views.EquipoList.as_view(), name = 'ListEquipo'),
    path(r'^equipo/(?P<pk>\d+)$', views.EquipoDetalle.as_view(), name = 'DetalleEquipo'),
    path(r'^nuevoEq$', views.EquipoCreate.as_view(), name = 'CreateEquipo'),
    path(r'^editarEq/(?P<pk>\d+)$', views.EquipoUpdate.as_view(), name = 'UpdateEquipo'),
    path(r'^borrarEq/(?P<pk>\d+)$', views.EquipoDelete.as_view(), name = 'DeleteEquipo')

]



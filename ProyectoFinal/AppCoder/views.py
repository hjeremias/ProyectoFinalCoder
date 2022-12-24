from django.http import HttpResponse
from django.shortcuts import render
from AppCoder.static import *
from AppCoder.forms import *
from AppCoder.models import *


# Create your views here.


def inicio(request):
      return render(request, 'AppCoder/inicio.html')


def CargaEquipo(request):
      
      if request.method == "POST":
      # Aqui me llega la informacion del html
            equipoFormulario = EquipoForm(request.POST)         

            if equipoFormulario.is_valid:
                  informacion = equipoFormulario.data
                  equipo = Equipo(nombre=informacion['nombreEquipo'], dt=informacion['dt'])
                  equipo.save()

                  return render(request, "AppCoder/inicio.html")
            else:
                  equipoFormulario = EquipoForm()
    
      else:
            equipoFormulario = EquipoForm()
    
      return render(request, "AppCoder/CargaEquipo.html", {"equipoFormulario": equipoFormulario})


def CargaJugador(request):
      if request.method == "POST":
      # Aqui me llega la informacion del html
            jugadorFormulario = JugadorForm(request.POST)
            #print(miFormulario)

            if jugadorFormulario.is_valid:
                  informacion = jugadorFormulario.data
                  jugador = Jugador(nombre=informacion['nombre'], equipo=informacion['equipo'])
                  jugador.save()
                  return render(request, "AppCoder/inicio.html")
            else:
                  jugadorFormulario = JugadorForm()
    
      else:
            jugadorFormulario = JugadorForm()
    
      return render(request, "AppCoder/CargaJugador.html", {"jugadorFormulario": jugadorFormulario})


def busquedaJugador(request):
      return render (request, "AppCoder/busquedaJugador.html")

def BuscarJugador (request):
      
      if request.GET["nombre"]:
            nombre = request.GET ['nombre']
            jugadores = Jugador.objects.filter(nombre__icontains = nombre)

            return render (request, "AppCoder/resultadosBusqueda.html", {"jugadores":jugadores, "nombre": nombre})
      
      else:
            return render (request, "AppCoder/busquedaJugador.html")



def BusquedaEquipos(request):
      return render (request, "AppCoder/BuscarEquipo.html")

     
def BuscarEquipo(request):
      if request.GET["nombre"]:
            nombre = request.GET ['nombre']
            equipos = Equipo.objects.filter(nombre__icontains = nombre)

            return render (request, "AppCoder/ResultadoBusquedaEquipos.html", {"equipos":equipos, "nombre": nombre})
      
      else:
            return render (request, "AppCoder/BuscarEquipo.html")
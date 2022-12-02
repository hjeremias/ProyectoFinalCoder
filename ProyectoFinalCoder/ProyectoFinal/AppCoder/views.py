from django.http import HttpResponse
from django.shortcuts import render
from AppCoder.static import *
from AppCoder.forms import *
from AppCoder.models import *


# Create your views here.


def inicio(request):
      return render(request, 'AppCoder/inicio.html')


#def Equipos(request):
#     return render(request, 'AppCoder/Equipo.html')

def Equipos(request):
      if request.method == "POST":
      # Aqui me llega la informacion del html
            miFormulario = EquipoForm(request.POST)
            #print(miFormulario)

            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  jugador = Equipo(nombre=informacion['nombre'], dt=informacion['dt'])
                  jugador.save()
                  return render(request, "AppCoder/inicio.html")
            else:
                  miFormulario = EquipoForm()
    
      else:
            miFormulario = EquipoForm()
    
      return render(request, "AppCoder/Equipo.html", {"miFormulario": miFormulario})


def Jugadores(request):
      if request.method == "POST":
      # Aqui me llega la informacion del html
            miFormulario = JugadorForm(request.POST)
            #print(miFormulario)

            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  jugador = Jugador(nombre=informacion['nombre'], equipo=informacion['equipo'])
                  jugador.save()
                  return render(request, "AppCoder/inicio.html")
            else:
                  miFormulario = JugadorForm()
    
      else:
            miFormulario = JugadorForm()
    
      return render(request, "AppCoder/Jugador.html", {"miFormulario": miFormulario})


def busquedaJugador(request):
      return render (request, "AppCoder/busquedaJugador.html")

def buscar (request):
      
      if request.GET["nombre"]:
            nombre = request.GET ['nombre']
            jugadores = Jugador.objects.filter(nombre__icontains = nombre)

            return render (request, "AppCoder/resultadosBusqueda.html", {"jugadores":jugadores, "nombre": nombre})
      
      else:
            return render (request, "AppCoder/busquedaJugador.html")

      #respuesta = f"Estoy buscando el jugador: {request.GET['nombre']}"

      return HttpResponse(respuesta)



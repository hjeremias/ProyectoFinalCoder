from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render
from AppCoder.static import *
from AppCoder.forms import *
from AppCoder.models import *


# Create your views here.


def inicio(request):
      return render(request, 'AppCoder/inicio.html')


def CargaEquipo(request):

      try:

            if request.method == "POST":
            # Aqui me llega la informacion del html
                  equipoFormulario = EquipoForm(request.POST)         

                  if equipoFormulario.is_valid():
                        informacion = equipoFormulario.data
                        equipo = Equipo(nombre=informacion['nombre'], dt=informacion['dt'])
                        equipo.save()

                        return render(request, "AppCoder/inicio.html")
                  else:
                        equipoFormulario = EquipoForm()
      
            else:
                  equipoFormulario = EquipoForm()
      
            return render(request, "AppCoder/CargaEquipo.html", {"equipoFormulario": equipoFormulario})

      except:
            return render(request, "AppCoder/Error.html")


def CargaJugador(request):

      try:

            if request.method == "POST":
            # Aqui me llega la informacion del html
                  jugadorFormulario = JugadorForm(request.POST)

                  if jugadorFormulario.is_valid():
                        jugadorFormulario.errors
                        informacion = jugadorFormulario.data
                        fecha_nacimiento = jugadorFormulario.cleaned_data['fechaNac']
                        pos = jugadorFormulario.cleaned_data['posicion']

                        jugador = Jugador(nombre=informacion['nombre'], equipo=informacion['equipo'], fechaNac=fecha_nacimiento, posicion=pos)
                        jugador.save()
                        return render(request, "AppCoder/inicio.html")
                  else:
                        jugadorFormulario = JugadorForm()
      
            else:
                  jugadorFormulario = JugadorForm()
      
            return render(request, "AppCoder/CargaJugador.html", {"jugadorFormulario": jugadorFormulario})

      except:
            return render(request, "AppCoder/Error.html")



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




##################################################################################################################
##################################################################################################################



                              #           CBV            #


#     JUGADORES     #

class JugadorList(ListView):

      model = Jugador
      template_name = 'AppCoder/jugador_list.html'


class JugadorDetalle(DetailView):

      model = Jugador
      template_name = 'AppCoder/jugador_detalle.html'

class JugadorCreate(CreateView):

      model = Jugador
      success_url = '/jugador/list'
      fields = ['nombre', 'equipo', 'fechaNac', 'posicion']

class JugadorUpdate(UpdateView):

      model = Jugador
      success_url = '/jugador/list'
      fields = ['nombre', 'equipo', 'fechaNac', 'posicion']

class JugadorDelete(DeleteView):

      model = Jugador
      success_url = '/jugador/list'



#     EQUIPOS     #

class EquipoList(ListView):

      model = Equipo
      template_name = 'AppCoder/equipo_list.html'


class EquipoDetalle(DetailView):

      model = Equipo
      template_name = 'AppCoder/equipo_detalle.html'

class EquipoCreate(CreateView):

      model = Equipo
      success_url = '/equipo/list'
      fields = ['nombre', 'dt']

class EquipoUpdate(UpdateView):

      model = Equipo
      success_url = '/equipo/list'
      fields = ['nombre', 'dt']

class EquipoDelete(DeleteView):

      model = Equipo
      success_url = '/equipo/list'
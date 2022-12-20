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

def Carga(request):
    if request.method == 'POST':
        form1 = EquipoForm(request.POST)
        form2 = JugadorForm(request.POST)
        if form1.is_valid() and form2.is_valid():
            nombre1 = form1.cleaned_data['nombre']
            equipo = form1.cleaned_data['equipo']
            nombre2 = form2.cleaned_data['nombre']
            dt = form2.cleaned_data['dt']
            # guardar los datos en la base de datos 
            return HttpResponse("Datos guardados correctamente")
    else:
        form1 = EquipoForm()
        form2 = JugadorForm()
    return render(request, 'AppCoder/Carga.html', {'form1': form1, 'form2': form2})


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

      #return HttpResponse(respuesta)



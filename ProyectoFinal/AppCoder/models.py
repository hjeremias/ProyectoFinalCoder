from django.db import models
import datetime

# Create your models here.


class Jugador (models.Model):
    nombre=models.CharField(max_length=40)
    equipo=models.CharField(max_length=40)
    fechaNac=models.DateField()
    posicion=models.CharField(max_length=40)

    def calcular_edad(self):
        hoy = datetime.date.today()
        edad = hoy.year - self.fechaNac.year
        if hoy < datetime.date(hoy.year, self.fechaNac.month, self.fechaNac.day):
            edad -= 1
        
        return edad
    

class Equipo (models.Model):
    nombre=models.CharField(max_length=40)
    dt=models.CharField(max_length=40)


from django.db import models

# Create your models here.


class Jugador (models.Model):
    nombre=models.CharField(max_length=40)
    equipo=models.CharField(max_length=40)

class Equipo (models.Model):
    nombre=models.CharField(max_length=40)
    dt=models.CharField(max_length=40)


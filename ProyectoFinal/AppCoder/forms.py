from django import forms
from django.forms.widgets import SelectDateWidget
from django.core.exceptions import ValidationError
from django.forms import DateField
 
class JugadorForm(forms.Form):
    nombre = forms.CharField() 
    equipo = forms.CharField()
    fechaNac = forms.DateField(label="Fecha de nacimiento", widget=SelectDateWidget(years=range(1900, 2020)) )
    posicion = forms.ChoiceField(
        #widget=forms.Select,
        choices=[
        ('Delantero', 'Delantero'),
        ('Mediocampista', 'Mediocampista'),
        ('Defensor', 'Defensor'),
        ('Arquero', 'Arquero'),
        ])

    
class EquipoForm(forms.Form):
    nombre = forms.CharField()
    dt = forms.CharField()




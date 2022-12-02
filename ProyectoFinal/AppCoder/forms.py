from django import forms
 
class JugadorForm(forms.Form):
    nombre = forms.CharField()
    equipo = forms.CharField()

class EquipoForm(forms.Form):
    nombre = forms.CharField()
    dt = forms.CharField()

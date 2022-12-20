from django import forms

class JugadorFormulario(forms.Form):
    nombre = forms.CharField()
    seleccion = forms.CharField()
    posicion = forms.CharField()
    clubactual = forms.CharField()
    dorsal = forms.IntegerField()



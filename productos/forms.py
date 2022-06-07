from django import forms

class Equipo_form(forms.Form):
    marca = forms.CharField(max_length=30)
    modelo = forms.CharField(max_length=30)
    disco =  forms.CharField(max_length=20)
    memoria = forms.CharField(max_length=20)
    precio = forms.FloatField()

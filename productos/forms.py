from django import forms


class Equipo_form(forms.Form):
    name =  forms.CharField(max_length=30)
    marca = forms.CharField(max_length=30)
    modelo = forms.CharField(max_length=30)
    disco =  forms.CharField(max_length=20)
    memoria = forms.CharField(max_length=20)
    precio = forms.FloatField()

class Periferico_form(forms.Form):
    name =  forms.CharField(max_length=30)
    tipo = forms.CharField(max_length=30)
    marca = forms.CharField(max_length=30)
    modelo =  forms.CharField(max_length=20)
    precio = forms.FloatField()

class Monitor_form(forms.Form):
    name =  forms.CharField(max_length=30)
    tipo = forms.CharField(max_length=30)
    marca = forms.CharField(max_length=30)
    modelo =  forms.CharField(max_length=20)
    resolucion = forms.CharField(max_length=20)
    conexion = forms.CharField(max_length=20)
    precio = forms.FloatField()
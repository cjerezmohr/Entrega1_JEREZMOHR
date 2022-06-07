import re
from django.shortcuts import render
from productos.models import *
from productos.forms import *

# Create your views here.
#def market(request):
    #equipo_nuevo = Desktop_notebook.objects.all()
    #externo_nuevo = Periferico.objects.all()
    #monitor_nuevo = Monitor.objects.all()
    #context = {'equipo_nuevo':equipo_nuevo,'externo_nuevo':externo_nuevo,'monitor_nuevo':monitor_nuevo}
    #return render(request, 'store.html', context=context)

def equipos(request):
    equipo_nuevo = Desktop_notebook.objects.all()
    context = {'equipo_nuevo':equipo_nuevo}
    return render(request, 'equipos.html', context = context)

def perifericos(request):
    externo_nuevo = Periferico.objects.all()
    context = {'externo_nuevo':externo_nuevo}
    return render(request, 'perifericos.html', context = context)

def monitor(request):
    monitor_nuevo = Monitor.objects.all()
    context = {'monitor_nuevo':monitor_nuevo}
    return render(request, 'monitores.html', context = context)

def crear_equipo(request):
    form = Equipo_form()
    context = {'form':form}
    return render(request, 'crear_equipo.html', context = context)

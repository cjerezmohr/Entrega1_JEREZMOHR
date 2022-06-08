import re
from django.shortcuts import render
from productos.models import *
from productos.forms import *
from django.http import HttpResponse

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
    if request.method == 'GET':
        form = Equipo_form()
        context = {'form':form}
        return render(request, 'crear_equipo.html', context = context)
    else:
        form = Equipo_form(request.POST)
        if form.is_valid():
            nuevo_equipo = Desktop_notebook.objects.create(
                name = form.cleaned_data['name'],
                marca = form.cleaned_data['marca'],
                modelo = form.cleaned_data['modelo'],
                disco = form.cleaned_data['disco'],
                memoria = form.cleaned_data['memoria'],
                precio = form.cleaned_data['precio'],
            )
            context ={'nuevo_equipo':nuevo_equipo}
        return render(request, 'crear_equipo.html', context = context)

def crear_periferico(request):
    if request.method == 'GET':
        form = Periferico_form()
        context = {'form':form}
        return render(request, 'crear_periferico.html', context = context)
    else:
        form = Periferico_form(request.POST)
        if form.is_valid():
            nuevo_periferico = Periferico.objects.create(
                name = form.cleaned_data['name'],
                tipo = form.cleaned_data['tipo'],
                marca = form.cleaned_data['marca'],
                modelo = form.cleaned_data['modelo'],
                precio = form.cleaned_data['precio'],
            )
            context ={'nuevo_periferico':nuevo_periferico}
        return render(request, 'crear_periferico.html', context = context)

def crear_monitores(request):
    if request.method == 'GET':
        form = Monitor_form()
        context = {'form':form}
        return render(request, 'crear_monitores.html', context = context)
    else:
        form = Monitor_form(request.POST)
        if form.is_valid():
            nuevo_monitor = Monitor.objects.create(
                name = form.cleaned_data['name'],
                tipo = form.cleaned_data['tipo'],
                marca = form.cleaned_data['marca'],
                modelo = form.cleaned_data['modelo'],
                resolucion = form.cleaned_data['resolucion'],
                conexion = form.cleaned_data['conexion'],
                precio = form.cleaned_data['precio'],
            )
            context ={'nuevo_monitor':nuevo_monitor}
        return render(request, 'crear_monitores.html', context = context)


def search_view(request):
    #print(request.GET)
    #equipo = Desktop_notebook.objects.get()
    equipo = Desktop_notebook.objects.filter(name__icontains = request.GET['search_view'])
    periferico=Periferico.objects.filter(name__icontains = request.GET['search_view'])
    monitor = Monitor.objects.filter(name__icontains = request.GET['search_view'])

    context = {'equipo':equipo,'periferico':periferico,'monitor':monitor}
    return render(request, 'search_view.html', context = context)
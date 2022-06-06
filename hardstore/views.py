from django.http import HttpResponse

from django.template import Template

from django.shortcuts import render
def index(request):
    return render(request, 'index.html')

def adios(request):
    return HttpResponse('adios')

def prueba_templates(request):
    context = {
        'nombre':'jimmy',
        'apodo':'patito'
    }
    return render(request, 'templates_1.html', context = context)
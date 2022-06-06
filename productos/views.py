from django.shortcuts import render
from productos.models import *

# Create your views here.
def market(request):
    equipo_nuevo = Desktop_notebook.objects.all()
    externo_nuevo = Periferico.objects.all()
    monitor_nuevo = Monitor.objects.all()
    context = {'equipo_nuevo':equipo_nuevo,'externo_nuevo':externo_nuevo,'monitor_nuevo':monitor_nuevo}
    return render(request, 'store.html', context=context)

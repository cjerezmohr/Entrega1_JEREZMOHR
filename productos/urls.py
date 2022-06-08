from django.urls import path

from productos.views import *


urlpatterns = [
    path('equipos/', equipos, name = 'equipos'),
    path('monitores/', monitor, name = 'monitores'),
    path('perifericos/', perifericos, name = 'perifericos'),
    path('crear-equipo/',crear_equipo, name = 'crear-equipo'),
    path('crear-periferico/',crear_periferico, name = 'crear-periferico'),
    path('crear-monitores/',crear_monitores, name = 'crear-monitores'),
    path('search_view/', search_view, name = 'search_view'),
]
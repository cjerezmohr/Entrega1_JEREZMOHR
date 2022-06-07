from django.urls import path

from productos.views import *


urlpatterns = [
    path('equipos/', equipos, name = 'equipos'),
    path('monitores/', monitor, name = 'monitores'),
    path('perifericos/', perifericos, name = 'perifericos'),
]  
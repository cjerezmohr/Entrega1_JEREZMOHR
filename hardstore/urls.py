"""hardstore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include
from hardstore.views import index
from hardstore.views import adios
from hardstore.views import prueba_templates
#from productos.views import market





urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name = 'index'),
    path('adios/', adios, name = 'adios'),
    path('templates/', prueba_templates, name = 'templates'),
    #path('store/', market, name = 'store'),
    path('store/', include('productos.urls')),
]

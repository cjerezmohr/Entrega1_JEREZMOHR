from django.contrib import admin

from productos.models import Desktop_notebook, Periferico, Monitor
# Register your models here.

admin.site.register(Desktop_notebook)
admin.site.register(Monitor)
admin.site.register(Periferico)
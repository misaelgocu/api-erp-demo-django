from django.contrib import admin
from ventas.models import Ventas, Empresas, Marcas, Sucursales


# Register your models here.
admin.site.register(Ventas)
admin.site.register(Empresas)
admin.site.register(Marcas)
admin.site.register(Sucursales)

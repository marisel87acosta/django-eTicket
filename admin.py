from django.contrib import admin
from eticketV1.apps.models import Categoria, Usuario, Infraccion, Infractor, Medicion, Multa, Vehiculo

# Register your models here.

admin.site.register(Usuario)
admin.site.register(Infractor)
admin.site.register(Infraccion)
admin.site.register(Categoria)
admin.site.register(Medicion)
admin.site.register(Multa)
admin.site.register(Vehiculo)

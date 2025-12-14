from django.contrib import admin
from .models import Animal, Adoptante, Solicitud

admin.site.register(Animal)
admin.site.register(Adoptante)
admin.site.register(Solicitud)
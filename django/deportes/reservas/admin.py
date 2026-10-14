from django.contrib import admin

from .models import ActividadDeportiva, Horario, Inscripcion

admin.site.register(ActividadDeportiva)
admin.site.register(Horario)
admin.site.register(Inscripcion)

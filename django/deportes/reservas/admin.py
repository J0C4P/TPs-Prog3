from django.contrib import admin

from .models import ActividadDeportiva, Horario, Inscripcion


@admin.register(ActividadDeportiva)
class ActividadDeportivaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'lugar', 'cupo')
    search_fields = ('nombre', 'lugar')
    list_filter = ('lugar',)
    ordering = ('nombre',)


@admin.register(Horario)
class HorarioAdmin(admin.ModelAdmin):
    list_display = ('actividad', 'dia', 'hora_inicio', 'hora_fin')
    search_fields = ('actividad__nombre',)
    list_filter = ('dia',)


@admin.register(Inscripcion)
class InscripcionAdmin(admin.ModelAdmin):
    list_display = ('apellido', 'nombre', 'dni', 'horario', 'estado', 'fecha_inscripcion')
    search_fields = ('apellido', 'nombre', 'dni')
    list_filter = ('estado',)
    date_hierarchy = 'fecha_inscripcion'

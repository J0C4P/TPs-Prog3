from django.db import models
from django.db.models import F, Q


class ActividadDeportiva(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    lugar = models.CharField(max_length=100)
    cupo = models.PositiveIntegerField()

    def __str__(self):
        return self.nombre


class Horario(models.Model):
    class Dia(models.TextChoices):
        LUNES = "Lunes", "Lunes"
        MARTES = "Martes", "Martes"
        MIERCOLES = "Miércoles", "Miércoles"
        JUEVES = "Jueves", "Jueves"
        VIERNES = "Viernes", "Viernes"
        SABADO = "Sábado", "Sábado"
        DOMINGO = "Domingo", "Domingo"

    actividad = models.ForeignKey(
        ActividadDeportiva,
        on_delete=models.CASCADE,
        related_name="horarios",
    )
    dia = models.CharField(max_length=10, choices=Dia.choices)
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()

    class Meta:
        constraints = [
            models.CheckConstraint(
                condition=Q(hora_fin__gt=F("hora_inicio")),
                name="horario_hora_fin_mayor_hora_inicio",
            ),
        ]

    def __str__(self):
        return (
            f"{self.actividad} - {self.dia} "
            f"{self.hora_inicio:%H:%M}-{self.hora_fin:%H:%M}"
        )


class Inscripcion(models.Model):
    class Estado(models.TextChoices):
        ACTIVA = "Activa", "Activa"
        CANCELADA = "Cancelada", "Cancelada"

    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dni = models.CharField(max_length=10)
    fecha_inscripcion = models.DateField(auto_now_add=True)
    estado = models.CharField(
        max_length=10,
        choices=Estado.choices,
        default=Estado.ACTIVA,
    )
    horario = models.ForeignKey(
        Horario,
        on_delete=models.CASCADE,
        related_name="inscripciones",
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["dni", "horario"],
                name="inscripcion_dni_horario_unico",
            ),
        ]

    def __str__(self):
        return f"{self.apellido}, {self.nombre} ({self.estado})"

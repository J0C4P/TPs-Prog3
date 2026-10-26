from django.contrib.auth.models import Group, Permission
from django.core.management.base import BaseCommand

# rol -> permisos por modelo
ROLES = {
    'Administradores': {
        'actividaddeportiva': ('add', 'change', 'delete', 'view'),
        'horario': ('add', 'change', 'delete', 'view'),
        'inscripcion': ('add', 'change', 'delete', 'view'),
    },
    'Secretaria': {
        'actividaddeportiva': ('view',),
        'horario': ('view',),
        'inscripcion': ('add', 'change', 'view'),
    },
    'Consulta': {
        'actividaddeportiva': ('view',),
        'horario': ('view',),
        'inscripcion': ('view',),
    },
}


class Command(BaseCommand):
    help = 'Crea los grupos (roles) y asigna sus permisos sobre los modelos de reservas.'

    def handle(self, *args, **options):
        for nombre, modelos in ROLES.items():
            grupo, _ = Group.objects.get_or_create(name=nombre)
            codenames = [f'{accion}_{modelo}' for modelo, acciones in modelos.items() for accion in acciones]
            permisos = Permission.objects.filter(
                content_type__app_label='reservas', codename__in=codenames
            )
            grupo.permissions.set(permisos)
            self.stdout.write(self.style.SUCCESS(f'{nombre}: {permisos.count()} permisos'))

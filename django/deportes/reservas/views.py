from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ActividadDeportivaForm
from .models import ActividadDeportiva


@permission_required('reservas.add_actividaddeportiva', raise_exception=True)
def agregar_actividad(request):
    if request.method == 'POST':
        form = ActividadDeportivaForm(request.POST)
        if form.is_valid():
            actividad = form.save()
            messages.success(request, f'La actividad «{actividad.nombre}» se registró correctamente.')
            return redirect('reservas:agregar_actividad')
    else:
        form = ActividadDeportivaForm()
    return render(request, 'reservas/agregar_actividad.html', {'form': form})


def lista_actividades(request):
    actividades = ActividadDeportiva.objects.all().order_by('nombre')
    return render(request, 'reservas/lista_actividades.html', {'actividades': actividades})


def detalle_actividad(request, actividad_id):
    actividad = get_object_or_404(ActividadDeportiva, pk=actividad_id)
    return render(request, 'reservas/detalle_actividad.html', {'actividad': actividad})

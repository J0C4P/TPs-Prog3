/* Ejercicio 4: muestra las actividades en la tabla de index.html.
   Los datos salen de sistemaDeportes, declarado en actividades.js (se carga antes, en el <head>) */

function mostrarActividades() {
  const cuerpoTabla = document.getElementById('cuerpo-tabla');
  const actividades = sistemaDeportes.listarActividades();

  actividades.forEach(actividad => {
    const fila = document.createElement('tr');

    const celdaNombre = document.createElement('td');
    celdaNombre.textContent = actividad.nombre;
    const celdaLugar = document.createElement('td');
    celdaLugar.textContent = actividad.lugar;
    const celdaDia = document.createElement('td');
    celdaDia.textContent = actividad.dia;
    const celdaHorario = document.createElement('td');
    celdaHorario.textContent = actividad.horario;
    const celdaCupo = document.createElement('td');
    celdaCupo.textContent = actividad.cupo;
    const celdaEstado = document.createElement('td');
    celdaEstado.textContent = actividad.estado;

    fila.append(celdaNombre, celdaLugar, celdaDia, celdaHorario, celdaCupo, celdaEstado);

    cuerpoTabla.appendChild(fila);
  });
}

mostrarActividades();

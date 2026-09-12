function Actividad(nombre, lugar, dia, horario, cupo, estado) {
  this.nombre = nombre;
  this.lugar = lugar;
  this.dia = dia;
  this.horario = horario;
  this.cupo = cupo;
  this.estado = estado;
}

class SistemaDeportes{
  constructor() {
    this.actividades = [];
  }

  agregarActividad(actividad) {
    this.actividades.push(actividad);
  }
  listarActividades() {
    return this.actividades;
  }
}

const sistemaDeportes = new SistemaDeportes();

sistemaDeportes.agregarActividad(new Actividad("Fútbol", "Cancha de fútbol del campus universitario", "Miércoles", "19:00", 20, "Disponible"));
sistemaDeportes.agregarActividad(new Actividad("Básquet", "Cancha de básquet del campus universitario", "Lunes", "16:00", 15, "Disponible"));
sistemaDeportes.agregarActividad(new Actividad("Vóley", "Cancha de vóley del campus universitario", "Viernes", "17:00", 20, "Disponible"));
sistemaDeportes.agregarActividad(new Actividad("Atletismo", "Estadio del campus universitario", "Martes", "20:00", 25, "Disponible"));
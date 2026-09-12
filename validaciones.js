function fechaNacimientoValida(fecha){
  if (!fecha) {
    return false;
  }
  const fechaActual = new Date();
  const fechaNacimiento = new Date(fecha);
  fechaActual.setHours(0, 0, 0, 0);
  return fechaNacimiento <= fechaActual;
}

function documentoValido(documento){
  return /^[0-9]{8}$/.test(documento);
}
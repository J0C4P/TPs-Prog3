const formulario = document.getElementById('formulario');
const cantidadParticipantes = document.getElementById('cantidadParticipantes');
const confirmarParticipantes = document.getElementById('confirmarParticipantes');
const contenedorParticipantes = document.getElementById('participantes');
const errorParticipantes = document.getElementById('error-participantes');

confirmarParticipantes.addEventListener('click', function(){
  const cantidad = parseInt(cantidadParticipantes.value, 10);

  if (isNaN(cantidad) || cantidad < 1 || cantidad > 10) {
    errorParticipantes.textContent = `Ingrese una cantidad de participantes entre ${1} y ${10}`;
    return;
  }

  errorParticipantes.textContent = '';
  contenedorParticipantes.innerHTML = '';

  for (let numero = 1; numero <= cantidad; numero++) {
    contenedorParticipantes.appendChild(crearBloqueParticipante(numero));
  }
});

function crearBloqueParticipante(numero) {
  const bloque = document.createElement('fieldset');
  bloque.className = 'participante';
  bloque.innerHTML = `
    <legend>Participante ${numero}</legend>
    <label for="apellido-nombre-${numero}">
      Apellido y Nombre:
    </label>
    <br>
    <input type="text" id="apellido-nombre-${numero}" name="apellido-nombre-${numero}" maxlength="100" required>
    <br>
    <label for="dni-${numero}">
      DNI:
    </label>
    <br>
    <input type="text" id="dni-${numero}" name="dni-${numero}" class="campo-dni" maxlength="8">
    <span class="error error-dni"></span>
    <br>
    <label for="fecha-nacimiento-${numero}">
      Fecha de nacimiento:
    </label>
    <br>
    <input type="date" id="fecha-nacimiento-${numero}" name="fecha-nacimiento-${numero}" class="campo-fecha-nacimiento">
    <span class="error error-fecha-nacimiento"></span>
    <br>
    <label for="sexo-${numero}">
      Sexo:
    </label>
    <br>
    <select id="sexo-${numero}" name="sexo-${numero}">
      <option value="masculino">Masculino</option>
      <option value="femenino">Femenino</option>
      <option value="no-binario">No binario</option>
    </select>
    <br>
    <label for="nivel-${numero}">
      Nivel:
    </label>
    <br>
    <select id="nivel-${numero}" name="nivel-${numero}">
      <option value="inicial">Inicial</option>
      <option value="intermedio">Intermedio</option>
      <option value="avanzado">Avanzado</option>
    </select>
  `;

  return bloque;
}

formulario.addEventListener('submit', function(event){
  event.preventDefault();

  const bloques = contenedorParticipantes.querySelectorAll('.participante');

  if (bloques.length === 0) {
    errorParticipantes.textContent = 'Genere al menos un participante antes de enviar la inscripción';
    return;
  }

  errorParticipantes.textContent = '';

  let formularioValido = true;

  bloques.forEach(bloque => {
    const dni = bloque.querySelector('.campo-dni');
    const fechaNacimiento = bloque.querySelector('.campo-fecha-nacimiento');
    const errorDni = bloque.querySelector('.error-dni');
    const errorFechaNacimiento = bloque.querySelector('.error-fecha-nacimiento');

    if (documentoValido(dni.value)) {
      errorDni.textContent = '';
    } else {
      errorDni.textContent = 'El DNI debe contener 8 dígitos';
      formularioValido = false;
    }

    if (fechaNacimientoValida(fechaNacimiento.value)) {
      errorFechaNacimiento.textContent = '';
    } else {
      errorFechaNacimiento.textContent = 'La fecha de nacimiento no puede ser posterior a la fecha actual';
      formularioValido = false;
    }
  });

  if (formularioValido) {
    formulario.submit();
  }
});

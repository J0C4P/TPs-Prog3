# Deportes Unca

Plataforma web para consultar actividades deportivas e inscribirse en ellas, desarrollada de forma incremental para la cátedra de Programación III (UNCa):

- **TP1** — estructura HTML5 de las páginas.
- **TP2** — hoja de estilos y maquetado responsive con Bootstrap.
- **TP3** (rama `Tp3-JavaScript`) — comportamiento dinámico del lado del cliente con JavaScript: validaciones de formulario, modelo de objetos para las actividades y generación de contenido por DOM.

## Estructura del proyecto

```
estilos.css              Hoja de estilos propia (tipografía Jost, tema oscuro)
JavaScript/
  actividades.js         Modelo de datos de las actividades
  tabla-actividades.js   Renderiza la tabla de actividades en el DOM
  validaciones.js        Funciones de validación reutilizables
  participantes.js       Generación dinámica de participantes + validación del formulario
html/
  index.html             Página principal: menú y tabla de actividades
  formulario.html        Inscripción a una actividad
  inscripciones.html     Inscripciones realizadas, con opción de cancelar
```

Los scripts siguen una convención simple: **lo que no toca el DOM se carga en el `<head>`; lo que manipula el DOM se carga al final del `<body>`**. Ninguna página tiene JavaScript embebido.

| Página | `<head>` | Fin del `<body>` |
|---|---|---|
| `index.html` | `actividades.js` | `tabla-actividades.js` |
| `formulario.html` | `validaciones.js` | `participantes.js` |

## JavaScript

### `validaciones.js`
Dos funciones puras (reciben un valor, devuelven un booleano, no tocan el DOM), lo que permite reutilizarlas para cualquier cantidad de campos:

- `fechaNacimientoValida(fecha)` — rechaza fechas posteriores a la actual. Normaliza la hora a medianoche para comparar solo por día.
- `documentoValido(documento)` — exige exactamente 8 dígitos mediante la expresión regular `/^[0-9]{8}$/`.

### `actividades.js`
- `Actividad(nombre, lugar, dia, horario, cupo, estado)` — función constructora de cada actividad deportiva.
- `SistemaDeportes` — clase con un array interno de actividades y los métodos `agregarActividad()` y `listarActividades()`.
- Instancia `sistemaDeportes` cargada con cuatro actividades: Fútbol, Básquet, Vóley y Atletismo.

### `tabla-actividades.js`
`mostrarActividades()` recorre el array del sistema y, por cada actividad, crea dinámicamente una fila (`createElement`, `textContent`, `append`) y la incorpora al `<tbody>` de la tabla. El `<tbody>` está vacío en el HTML: las filas existen solo en el DOM.

### `participantes.js`
- Al presionar "Agregar Participante" lee la cantidad ingresada (validando en JavaScript que esté entre 1 y 10, porque los atributos `min`/`max` solo actúan al enviar el formulario) y genera un bloque por participante con Apellido y Nombre, DNI, Fecha de nacimiento, Sexo y Nivel. Cada bloque recibe ids únicos con el número de participante, y el contenedor se vacía antes de regenerar para que los bloques no se acumulen.
- Al enviar el formulario recorre **todos** los bloques generados, valida el DNI y la fecha de nacimiento de cada uno con las funciones de `validaciones.js` y muestra los mensajes de error junto al campo correspondiente. El envío se bloquea con `event.preventDefault()` mientras haya algún dato inválido.

Los campos de cada participante se ubican por clase (`.campo-dni`, `.campo-fecha-nacimiento`) y no por id, de modo que la misma validación sirve para uno o para diez participantes.

## Estilos

- Bootstrap 5.3.8 desde CDN para la grilla (`container`), las tablas (`table`, `table-striped`) y el desplazamiento horizontal de tablas en pantallas angostas (`table-responsive`).
- `estilos.css` define el tema propio: tipografía Jost, fondo oscuro, colores de títulos y enlaces, estilos del formulario, de los bloques de participante generados por JS y de los mensajes de validación. Las tablas se tematizan mediante las variables CSS de Bootstrap (`--bs-table-*`).

## Cómo ejecutarlo

Abrir `html/index.html` en un navegador web. Requiere conexión a Internet para descargar Bootstrap y la tipografía Jost desde sus CDN.

Para probar las validaciones en `html/formulario.html` hay que tildar "Acepto las condiciones de inscripción": ese checkbox tiene el atributo `required`, y mientras no esté tildado el navegador cancela el envío y el evento `submit` no se dispara.

## Limitaciones conocidas

- **No hay backend ni persistencia.** Nada de lo que se carga se guarda: la información se pierde al recargar la página.
- **El envío exitoso del formulario no lleva a ninguna parte.** Si todas las validaciones pasan, el formulario se envía a `pagina3.html` (el `action` heredado del TP1), que no existe en el proyecto, por lo que el navegador muestra un error de página no encontrada. La validación del lado del cliente —que es el objetivo del TP3— funciona correctamente; lo que falta es la página de destino o el procesamiento del lado del servidor.
- La tabla de `inscripciones.html` y los datos de la actividad en el formulario siguen siendo contenido estático, cargado a mano en el HTML.

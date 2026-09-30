# Deportes Unca

Repositorio de los trabajos prácticos de la cátedra de Programación III (UNCa). Los primeros trabajos construyen de forma incremental una plataforma web para consultar actividades deportivas e inscribirse en ellas; el último es una serie de ejercicios de Python independientes del sitio:

- **TP1** — estructura HTML5 de las páginas.
- **TP2** — hoja de estilos y maquetado responsive con Bootstrap.
- **TP3** (rama `Tp3-JavaScript`) — comportamiento dinámico del lado del cliente con JavaScript.
- **TP4** (rama `Tp4-Python`, esta rama) — introducción al lenguaje Python mediante ejercicios sueltos.

## TP4 — Introducción al lenguaje Python

Los ejercicios del TP4 **no forman parte del sitio web**: son cuatro programas de consola independientes entre sí, cada uno en su propio archivo dentro de la carpeta `Python/`. No comparten código, no dependen del HTML/CSS/JavaScript de los TP anteriores y no requieren librerías externas ni entorno virtual (solo Python 3).

Consigna: [`MaterialReferencia/TP4.pdf`](MaterialReferencia/TP4.pdf). Guía de desarrollo: [`GUIA-TP4-PYTHON.md`](GUIA-TP4-PYTHON.md).

```
Python/
  ejercicio1.py          Validación de entrada y búsqueda en una lista
  ejercicio2.py          Conjuntos de usuarios y administradores
  ejercicio3.py          Registro de usuarios en diccionarios
  ejercicio4.py          Inventario de instrumentos musicales
```

### Ejercicio 1 — Validación de entrada y búsqueda en una lista
Pide un número entero del 0 al 9 y repite la solicitud mientras el valor no sea un entero o esté fuera de rango (`try/except ValueError` dentro de un `while True`). Cuando el valor es válido, usa el operador `in` para avisar si el número está o no en una lista predefinida.

### Ejercicio 2 — Conjuntos de usuarios y administradores
Crea los conjuntos `usuarios` y `administradores`, quita a Juan de administradores con `.discard()`, agrega a Marcos como administrador (sigue en `usuarios`) y lista a cada usuario indicando si es administrador o no.

### Ejercicio 3 — Registro de información en un diccionario
Solicita nombre, edad, dirección y teléfono, y guarda cada usuario en un diccionario `usuario_info`; los diccionarios se acumulan en una lista. La carga termina al dejar el nombre vacío. Al final muestra cada usuario en formato clave-valor.

### Ejercicio 4 — Inventario de instrumentos musicales
Modela sucursales que contienen instrumentos (ID, precio y tipo: Percusión, Viento o Cuerda) con las clases `Instrumento` y `Sucursal`, y una lista global `sucursales`. Implementa las cuatro operaciones pedidas:

- `listarInstrumentos()` — muestra en consola sucursal, ID, precio y tipo de cada instrumento.
- `instrumentosPorTipo(tipo)` — devuelve la lista de instrumentos de ese tipo.
- `borrarInstrumento(id)` — elimina el instrumento de la sucursal donde se encuentre (devuelve `False` si el ID no existe).
- `porcInstrumentosPorTipo(sucursal)` — devuelve el porcentaje de cada tipo en la sucursal indicada.

Al final del archivo hay datos de prueba (dos sucursales) y una demostración que llama a cada función.

### Cómo ejecutarlos

Desde la raíz del repositorio, con Python 3 instalado:

```
python Python/ejercicio1.py
python Python/ejercicio2.py
python Python/ejercicio3.py
python Python/ejercicio4.py
```

Los ejercicios 1 y 3 piden datos por teclado; los ejercicios 2 y 4 se ejecutan solos y muestran su resultado por consola.

## Sitio web (TP1 a TP3)

El sitio sigue en el repositorio, sin cambios en esta rama. Su estructura:

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

Para verlo, abrir `html/index.html` en un navegador (requiere conexión a Internet para Bootstrap 5.3.8 y la tipografía Jost desde sus CDN). El detalle del funcionamiento de los scripts está en la rama `Tp3-JavaScript` y en [`GUIA-TP3-JAVASCRIPT.md`](GUIA-TP3-JAVASCRIPT.md).

Limitaciones conocidas del sitio: no hay backend ni persistencia (los datos se pierden al recargar), y el envío exitoso del formulario apunta a `pagina3.html`, que no existe en el proyecto.

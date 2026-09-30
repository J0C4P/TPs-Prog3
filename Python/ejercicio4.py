TIPOS = ["Percusión", "Viento", "Cuerda"]


class Instrumento:
    def __init__(self, id, precio, tipo):
        self.id = id
        self.precio = precio
        self.tipo = tipo


class Sucursal:
    def __init__(self, nombre):
        self.nombre = nombre
        self.instrumentos = []


def listarInstrumentos():
    for sucursal in sucursales:
        for instrumento in sucursal.instrumentos:
            print(f"{sucursal.nombre} | {instrumento.id} | ${instrumento.precio} | {instrumento.tipo}")


def instrumentosPorTipo(tipo):
    lista = []
    for sucursal in sucursales:
        for instrumento in sucursal.instrumentos:
            if instrumento.tipo == tipo:
                lista.append(instrumento)
    return lista


def borrarInstrumento(id):
    for sucursal in sucursales:
        for instrumento in sucursal.instrumentos:
            if instrumento.id == id:
                sucursal.instrumentos.remove(instrumento)
                return True
    return False


def porcInstrumentosPorTipo(nombre_sucursal):
    for sucursal in sucursales:
        if sucursal.nombre == nombre_sucursal:
            total = len(sucursal.instrumentos)
            porcentajes = {}
            for tipo in TIPOS:
                cantidad = 0
                for instrumento in sucursal.instrumentos:
                    if instrumento.tipo == tipo:
                        cantidad += 1
                porcentajes[tipo] = cantidad * 100 / total if total > 0 else 0
            return porcentajes
    return None


# Datos de prueba
centro = Sucursal("Centro")
centro.instrumentos.append(Instrumento("P001", 1500, "Percusión"))
centro.instrumentos.append(Instrumento("C001", 3200, "Cuerda"))
centro.instrumentos.append(Instrumento("C002", 2800, "Cuerda"))
centro.instrumentos.append(Instrumento("V001", 900, "Viento"))

norte = Sucursal("Norte")
norte.instrumentos.append(Instrumento("V002", 1100, "Viento"))
norte.instrumentos.append(Instrumento("P002", 2000, "Percusión"))

sucursales = [centro, norte]

print("Todos los instrumentos:")
listarInstrumentos()

print("\nInstrumentos de tipo Cuerda:")
for instrumento in instrumentosPorTipo("Cuerda"):
    print(instrumento.id, instrumento.precio)

print("\nBorrar C002:", "borrado" if borrarInstrumento("C002") else "no encontrado")
print("Borrar XXXX:", "borrado" if borrarInstrumento("XXXX") else "no encontrado")

print("\nPorcentajes en Centro:")
porcentajes = porcInstrumentosPorTipo("Centro")
if porcentajes is None:
    print("La sucursal no existe")
else:
    for tipo, porcentaje in porcentajes.items():
        print(f"{tipo}: {porcentaje:.1f}%")

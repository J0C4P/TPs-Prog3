lista_usuarios = []

while True:
    print("Usuario Nuevo:")
    print("-------------------")
    print("(Deja el nombre vacio para cancelar el registro)")
    input_nombre = input("Ingrese el nombre: ")
    if input_nombre == "":
        break
    input_edad = input("Ingrese la edad: ")
    input_dir = input("Ingrese la dirección: ")
    input_tel = input("Ingrese el teléfono: ")

    usuario_info = {
        "nombre": input_nombre, "edad": input_edad, "dirección": input_dir, "teléfono": input_tel 
    }

    lista_usuarios.append(usuario_info)

print("---------------------------")
print("Usuarios Registrados:")
print("---------------------------")
for usuario in lista_usuarios:
    for clave, valor in usuario.items():
        print(f"{clave}: {valor}")
    print("---------------------------")


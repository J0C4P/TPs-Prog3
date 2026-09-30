usuarios = set(["Marcela", "David", "Elvira", "Juan", "Marcos"])
administradores = set(["Juan", "Marcela"])

administradores.discard("Juan")
administradores.add("Marcos")

for usuario in usuarios:
    esAdmin = False
    if usuario in administradores:
        esAdmin = True
    print(f"{usuario:<8} {'(Admin)' if esAdmin else '(Usuario)'}")
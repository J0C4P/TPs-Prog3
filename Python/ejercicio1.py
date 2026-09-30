rango = range(0,10,1)
lista = [2,7,4,1,3,12]

while True:
    num_input = input("Ingrese un número:")
    try:
        numero = int (num_input)
    except ValueError:
        print("El valor ingresado no es un número valido, intentalo de nuevo")
        continue
    if numero not in rango:
      print("El número ingresado NO está en el rango permitido, intentalo de nuevo")
      continue
    else:
      if numero in lista:
          print("El número ingresado está en la lista")
      else:
          print("El número ingresado NO está en la lista")
    break
"""calculadora"""

print("Bienvenidos a la calculadora")
print("Para salir escribe salir")
print("Las operaciones son suma, resta, multiplicación y división")

numero = ""

while True:
    if not numero:
        numero = input("ingrese número: ")
        if numero.lower == ( "salir"):
            break
        numero = int(numero)
    operacion = input("Ingrese operación ")
    if operacion.lower() == "salir":
        break
    numero_2 = input("Ingresa siguiente número: ")
    if numero_2.lower() == "salir":
        break
    numero_2 = int(numero_2)

    if operacion.lower() == "suma":
        numero += numero_2
    elif operacion.lower() == "resta":
        numero -= numero_2
    elif operacion.lower() == "multiplicación":
        numero *= numero_2
    elif operacion.lower() == "división":
        numero /= numero_2
    else:
        print("La operación no es válida, vuelve a intentar.")
    
    print(f"El resultado de la operación es {numero}")


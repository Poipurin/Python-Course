saludo = "Hola global"

def saludito():
    global saludo
    saludo = "Hola Mundo"
    print(saludo)

def saludarRata():
    saludo = "Hola Rata"
    print(saludo)

print(saludo)
saludito()
saludarRata()
print(saludo)

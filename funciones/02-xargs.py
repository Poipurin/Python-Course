def suma(*numeros):
    resultado = 0
    for numero in numeros:
        resultado += numero
    print(resultado)
   

suma(2, 5)
suma(2, 5, 10)
suma(2, 5, 10, 300)
suma(2, 5, 10, 300, 6)

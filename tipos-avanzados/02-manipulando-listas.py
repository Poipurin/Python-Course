mascotas = ["Wolfgang","Pelusa", "Pulga", "Copito"]
print(mascotas[0])
mascotas[0] = "Bicho"
print(mascotas[:3])
print(mascotas[-1])
print(mascotas[::2]) #pares

numeros = list(range(21))
print(numeros[1::2])#impares, empieza desde el siguiente index
numeros_2 = list(range(1, 21))# se redacta acá
print(numeros_2[::2])
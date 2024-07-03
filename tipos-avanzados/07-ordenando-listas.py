numeros = [2, 4, 1, 45, 75, 22]

#numeros.sort(reverse=True)
numeros_2 = sorted(numeros, reverse=True)

print(numeros)
print(numeros_2)

usuarios = [["Chanchito", 4], ["Brownie", 1], ["Berlín", 5]]

def ordena(elemento):
    return elemento[1]

usuarios.sort(key=ordena, reverse=True)
print(usuarios)
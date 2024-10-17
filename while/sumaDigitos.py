numero = input("Ingrese un número: ")

suma = 0
indice = 0

while indice < len(numero):
    suma += int(numero[indice])
    indice += 1  

print("La suma de los dígitos es:", suma)
def contarVocales(cadena):
    vocales = "aeiouAEIOU"
    contador = 0
    indice = 0  

    while indice < len(cadena):
        if cadena[indice] in vocales:
            contador += 1
        indice += 1  
    return contador

cadenaUsuario = input("Ingrese una cadena: ")

contVocales = contarVocales(cadenaUsuario)
print(f"Número de vocales en la cadena: {contVocales}")
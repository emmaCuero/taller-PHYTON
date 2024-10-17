def buscar_elemento(lista, elemento):
    
    for caracter in lista:
        if caracter == elemento:
            return True
    return False


listaCaracteres = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
elemento_a_buscar = input("ingrese un elemento a buscar: " )
        

if buscar_elemento(listaCaracteres, elemento_a_buscar):
    print(f"El elemento '{elemento_a_buscar}' se encuentra en la lista.")
else:
    print(f"El elemento '{elemento_a_buscar}' no se encuentra en la lista.")
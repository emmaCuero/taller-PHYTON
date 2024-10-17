tupla = [(1, 3), (4, 1), (2, 2), (5, 0)]

# Ordenar la lista de tuplas según el segundo elemento
listaOrdenada = sorted(tupla, key=lambda x: x[1])

# Mostrar el resultado
print(listaOrdenada)
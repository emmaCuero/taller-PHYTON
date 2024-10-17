tamaño = 8

for fila in range(tamaño):
    linea = ''
    for columna in range(tamaño):
        if (fila + columna) % 2 == 0:
            linea += ' B'  # Casilla blanca
        else:
            linea += ' N'  # Casilla negra
    print(linea)
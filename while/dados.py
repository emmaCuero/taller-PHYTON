import random

resultado = 0
# Contador para llevar el número de tiradas
tiradas = 0

while resultado != 6:
    resultado = random.randint(1, 6)  # Tirar el dado
    tiradas += 1  # Incrementar el contador de tiradas
    print(f"Tirada {tiradas}: {resultado}")  # Mostrar el resultado de la tirada

print(f"Se obtuvo un 6 después de {tiradas} tiradas")
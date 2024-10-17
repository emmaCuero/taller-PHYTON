cadena = input("Ingresa una cadena: ")

cadena_invertida = ""

# Usar un ciclo for para recorrer la cadena desde el final hasta el principio
for i in range(len(cadena) - 1, -1, -1):
    cadena_invertida += cadena[i]  # Agregar cada carácter a la cadena invertida
    
print("La cadena invertida es:", cadena_invertida)
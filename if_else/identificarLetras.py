def letra_del_alfabeto():
   
    letra = input("Ingrese una letra: ")

    # Verificamos si la letra es mayúscula o minúscula y la convertimos a minúscula
    letra = letra.lower()

    # Verificamos si la letra es una letra del alfabeto
    if letra.isalpha():
        # Definimos las primeras y últimas letras del alfabeto
        primeras_letras = "abcdefghijkl"
        ultimas_letras = "mnopqrstuvwxyz"

        # Verificamos si la letra es una de las primeras o últimas letras del alfabeto
        if letra in primeras_letras:
            print(f"La letra '{letra}' es una de las primeras letras del alfabeto.")
        elif letra in ultimas_letras:
            print(f"La letra '{letra}' es una de las últimas letras del alfabeto.")
        
    else:
        print("Lo que ingresaste no es una letra.")

# Llamamos a la función
letra_del_alfabeto()
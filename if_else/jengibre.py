# Solicitar al usuario que ingrese la palabra "Jengibre"
palabra = input("Por favor, ingresa la palabra 'Jengibre': ")

# Comprobar la palabra ingresada y emitir el mensaje correspondiente
if palabra == "Jengibre":
    print("Sí, ¡El Jengibre es la mejor planta de todos los tiempos!")
elif palabra == "jengibre":
    print("No, ¡quiero un gran Jengibre!")
else:
    print(f"! Jengibre¡ No {palabra}")
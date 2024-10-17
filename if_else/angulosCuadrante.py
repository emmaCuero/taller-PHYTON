def cuadrante_angulo(angulo):
    if angulo < 0 or angulo > 360:
        return "El ángulo debe estar entre 0 y 360 grados."
    
    if 0 <= angulo < 90 or angulo == 360:
        return "El ángulo está en el primer cuadrante."
    elif 90 <= angulo < 180:
        return "El ángulo está en el segundo cuadrante."
    elif 180 <= angulo < 270:
        return "El ángulo está en el tercer cuadrante."
    elif 270 <= angulo < 360:
        return "El ángulo está en el cuarto cuadrante."

angulo_input = float(input("Ingrese el valor del ángulo en grados: "))
resultado = cuadrante_angulo(angulo_input)
print(resultado)
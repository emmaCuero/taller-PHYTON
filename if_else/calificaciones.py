def clasificar_rendimiento(calificacion):
    if calificacion > 4.5:
        return "Excelente"
    elif 3.5 <= calificacion <= 4.5:
        return "Bueno"
    elif 3 <= calificacion < 3.5:
        return "Regular"
    else:
        return "Insuficiente"

# Ejemplo de uso
calificacion_estudiante = float(input("Ingrese la calificación del estudiante: "))
rendimiento = clasificar_rendimiento(calificacion_estudiante)
print(f"El rendimiento del estudiante es: {rendimiento}")
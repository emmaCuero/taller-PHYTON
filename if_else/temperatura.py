def clasificarTemperatura(temp):
    if temp < 10:
        return "Frio"
    elif 10 <= temp <= 25:
        return "Templado"
    else:
        return "Cálido"


temp = float(input("Ingrese la temperatura en grados Celsius: "))
print(clasificarTemperatura(temp))
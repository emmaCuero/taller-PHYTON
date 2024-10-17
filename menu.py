import random


def piramide():
    altura = 5

    for i in range(altura):
        espacios = altura - i
        asteriscos =  i + 1
        
        print(' ' * espacios + ' *' * asteriscos)
    menu()


def buscarCuadrante():
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
    menu()


def filtrarMayores():
    listaNumeros = [5, 12, 7, 19, 3, 15, 8, 11, 100, 1]
    print(f"la lista de números es:  \n{listaNumeros}")


    # Filtrar números mayores a 10
    numeros_mayores_a_10 = list(filter(lambda x: x > 10, listaNumeros))

    print(f"los numeros mayores a 10 son:  \n{numeros_mayores_a_10}")

    menu()

def lanzarDados():
   
    resultado = 0
    # Contador para llevar el número de tiradas
    tiradas = 0

    while resultado != 6:
        resultado = random.randint(1, 6)  # Tirar el dado
        tiradas += 1  # Incrementar el contador de tiradas
        print(f"Tirada {tiradas}: {resultado}")  # Mostrar el resultado de la tirada

    print(f"Se obtuvo un 6 después de {tiradas} tiradas")
    menu()


def menu():
        print()
        print("Bienvenido")
        print("1. ejercicio FOR piramide")
        print("2. ejercicio if_else cuandranteAngulo")
        print("3. ejercicio Lambda filtarMayores")
        print("4. ejercicio While lanzarDados")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")
       
        if opcion == '1':
            piramide()
        elif opcion ==  '2':
            buscarCuadrante()
        elif  opcion == '3':
             filtrarMayores()
        elif  opcion == '4':
              lanzarDados()
        elif opcion == '5':
            print("Hasta luego")
            exit()
        else:
            print("")
            print("SELECCIONE UNA OPCION VALIDA")
            menu()
menu()
from ejercicio4 import *
from ejercicio5 import *
from funciones_generales import *

def imprimir_menu():
    print("Seleccione el ejercicio que desea ejecutar:")
    print("1. Ejercicio 1")
    print("2. Ejercicio 2")
    print("3. Ejercicio 3")
    print("4. Ejercicio 4")
    print("5. Ejercicio 5")
    print("6. Ejercicio Adicional")
    print("7. Salir")

def menu_principal():
    seleccion = int(input("Seleccione un ejercicio: "))
    match seleccion:
        case 1:
            print("Ejercicio 1")
            # Llamar a la función del ejercicio 1
            pass
        case 2:
            print("Ejercicio 2")
            # Llamar a la función del ejercicio 2
            pass
        case 3:
            print("Ejercicio 3")
            # Llamar a la función del ejercicio 3
            pass
        case 4:
            print("Ejercicio 4")
            # Llamar a la función del ejercicio 4
            menu4()
        case 5:
            print("Ejercicio 5")
            # Llamar a la función del ejercicio 5
            menu5()
        case _:
            print("Selección inválida. Intente nuevamente.")

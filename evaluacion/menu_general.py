from evaluacion.menus.ejercicio4 import *
from evaluacion.menus.ejercicio5 import *
from evaluacion.menus.ejercicio3 import *
from evaluacion.menus.ejercicio2 import *
from evaluacion.menus.ejercicio1 import *
from evaluacion.menus.ejercicio_adicional import *
from funciones_adicionales.funciones_generales import *



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
    while True:
        imprimir_menu()
        seleccion = int(input("Seleccione un ejercicio: "))
        match seleccion:
            case 1:
                print("Ejercicio 1")
                menu1()
                esperar_usuario()
            case 2:
                print("Ejercicio 2")
                menu2()
                esperar_usuario()
            case 3:
                print("Ejercicio 3")
                menu3()
                esperar_usuario()
            case 4:
                print("Ejercicio 4")
                # Llamar a la función del ejercicio 4
                menu4()
                esperar_usuario()
            case 5:
                print("Ejercicio 5")
                # Llamar a la función del ejercicio 5
                menu5()
                esperar_usuario()
            case 6:
                print("Ejercicio Adicional")
                # Llamar a la función del ejercicio adicional
                menu_adicional()
                esperar_usuario()
            case 7:
                print("Saliendo del programa...")
                esperar_usuario()
                return
            case _:
                print("Selección inválida. Intente nuevamente.")
                esperar_usuario()
                return


from evaluacion_pila_cola.models.cola import Cola
from evaluacion_pila_cola.models.pila import Pila
from funciones.funciones_menu import *

def main():
    """
    Función principal para ejecutar el programa.
    """
    cola = Cola()
    pila = Pila()

    while True:
        imprimir_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_dato(cola)
        elif opcion == "2":
            eliminar_dato(cola)
        elif opcion == "3":
            organizar_datos(cola, pila)
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")
from models.cola_prioridad import *
from funciones_generales import *


def mostrar_menu():
    """Muestra el menú de opciones al usuario."""
    print("\n--- Menú de Cola de Prioridad ---")
    print("1. Agregar elemento a la cola")
    print("2. Desencolar elemento (siguiente por prioridad)")
    print("3. Mostrar todos los elementos en cola")
    print("4. Mostrar número de elementos en cola")
    print("5. Salir")


def agregar_elemento(cola):
    """Permite al usuario agregar un nuevo elemento a la cola."""
    print("\n--- Agregar nuevo elemento ---")
    nombre = input("Ingrese el nombre del elemento: ")
    while True:
        try:
            prioridad = int(input("Ingrese la prioridad (número entero, menor = más prioritario): "))
            break
        except ValueError:
            print("Error: La prioridad debe ser un número entero. Intente nuevamente.")

    elemento = Elemento(nombre, prioridad)
    cola.encolar(elemento)
    print(f"Elemento '{nombre}' agregado con prioridad {prioridad}.")


def desencolar_elemento(cola):
    """Desencola y muestra el elemento con mayor prioridad."""
    print("\n--- Desencolar elemento ---")
    if cola.esta_vacia():
        print("La cola está vacía. No hay elementos para desencolar.")
    else:
        elemento = cola.desencolar()
        print(f"Elemento desencolado: {elemento}")


def mostrar_elementos(cola):
    """Muestra todos los elementos en la cola ordenados por prioridad."""
    print("\n--- Elementos en la cola ---")
    if cola.esta_vacia():
        print("La cola está vacía.")
    else:
        print(cola)


def mostrar_cantidad(cola):
    """Muestra la cantidad de elementos en la cola."""
    print(f"\nHay {len(cola)} elementos en la cola.")


def menu4():
    """Función principal del programa interactivo."""
    cola = ColaPrioridad()
    print("Bienvenido al sistema de Cola de Prioridad")

    while True:
        mostrar_menu()
        opcion = int(input("Seleccione una opción: "))

        match opcion:
            case 1:
                agregar_elemento(cola)
                esperar_usuario()
            case 2:
                desencolar_elemento(cola)
                esperar_usuario()
            case 3:
                mostrar_elementos(cola)
                esperar_usuario()
            case 4:
                mostrar_cantidad(cola)
                esperar_usuario()
            case 5:
                print("Saliendo del programa...")
                esperar_usuario()
                break
            case _:
                print("Opción no válida. Por favor ingrese un número del 1 al 5.")
                esperar_usuario()

if __name__ == "__main__":
    menu4()
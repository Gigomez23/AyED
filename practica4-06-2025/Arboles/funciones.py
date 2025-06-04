"""
archivo: funciones.py
Este módulo contiene funciones para manejar un árbol binario, incluyendo la inserción de nodos, búsqueda de valores y recorridos del árbol.
"""

import os, platform
from arboles import ArbolBin

def limpiar_consola():
    """Limpia la consola dependiendo del sistema operativo."""
    sistema = platform.system()
    if sistema == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def esperar_usuario():
    """Espera a que el usuario presione Enter para continuar."""
    print("Presione Enter para continuar...")
    input()
    limpiar_consola()

def imprimir_menu():
    """Imprime el menú de opciones para el usuario.
    """
    print("1. Insertar nodo")
    print("2. Buscar nodo")
    print("3. Recorrer en orden")
    print("4. Recorrer preorden")
    print("5. Recorrer postorden")
    print("6. Salir")
    
def menu():
    """Función principal que muestra el menú y maneja las opciones del usuario.
    """
    arbol = ArbolBin()
    
    while True:
        imprimir_menu()
        opcion = input("Seleccione una opción: ")
        
        match opcion:
            case '1':
                valor = int(input("Ingrese el valor del nodo a insertar: "))
                arbol.insertar(valor)
                print(f"Nodo {valor} insertado.")
                esperar_usuario()
            
            case '2':
                valor = int(input("Ingrese el valor del nodo a buscar: "))
                encontrado = arbol.buscar(valor)
                if encontrado:
                    print(f"Nodo {valor} encontrado.")
                else:
                    print(f"Nodo {valor} no encontrado.")
                    esperar_usuario()
            
            case '3':
                print("Recorrido en orden:")
                arbol.recorrido_inorden(arbol.raiz)
                print()
                esperar_usuario()
            
            case '4':
                print("Recorrido preorden:")
                arbol.recorrido_preorden(arbol.raiz)
                print()
                esperar_usuario()
            
            case '5':
                print("Recorrido postorden:")
                arbol.recorrido_postorden(arbol.raiz)
                print()
                esperar_usuario()
            
            case '6':
                print("Saliendo del programa.")
                break
                
            
            case _:
                print("Opción no válida. Intente de nuevo.")
                esperar_usuario()
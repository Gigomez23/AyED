"""
funcion.py

Este modulo contiene las funciones generales para el ejercisio de clase involucrando pilas.

Funciones:
    limpiar_consola: Limpia la consola dependiendo del sistema operativo.
    esperar_usuario: Espera a que el usuario presione Enter para continuar.
    mostrar_menu: Muestra el menú principal del editor de texto y devuelve la opción seleccionada por el usuario.
    main: Función principal que ejecuta el programa.
"""

import os
import platform
from models import *

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


def mostrar_menu():
    """Muestra las opcoines del menu principal."""
    print("Seleccione una opción:")
    print("1. Agregar Dato (Push)")
    print("2. Eliminar Dato (Pop)")
    print("3. Organizar de pares a impares")
    print("4. Organizar de mayor a menor")
    print("5. Convertir a binario")
    print("6. Mostrar pila")
    print("7. Salir")
    return int(input("Seleccione una opción: "))

def main():
    """
    Función principal que ejecuta el programa.
    """
    tamano = int(input("Ingrese el tamaño de la pila: "))
    pila = Pila(tamano)
    while True:
        opcion = mostrar_menu()

        try:
            match opcion:
                case 1:
                    dato = int(input("Ingrese el dato a agregar: "))
                    pila.push(dato)
                    esperar_usuario()

                case 2:
                    if pila.is_empty():
                        print("Pila vacía, no se puede eliminar")
                        continue
                    else:
                        dato = pila.pop()
                        print(f"Elemento eliminado: {dato}")
                    esperar_usuario()

                case 3:
                    if pila.is_empty():
                        print("Pila vacía, no se puede organizar")
                        continue
                    else:
                        pila.organizar_pares_impares()
                        print("Pila organizada de pares a impares")
                        print(pila)
                    esperar_usuario()

                case 4:
                    if pila.is_empty():
                        print("Pila vacía, no se puede organizar")
                        continue
                    else:
                        pila.ordenar_mayor_menor()
                        print("Pila organizada de mayor a menor")
                        print(pila)
                    esperar_usuario()

                case 5:
                    numero = int(input("Ingrese un número para convertir a binario: "))
                    if numero < 0:
                        print("Número negativo, no se puede convertir a binario")
                        continue
                    else:
                        binario = Convbinario(numero)
                        print(f"El número {numero} en binario es: {binario}")
                    esperar_usuario()

                case 6:
                    if pila.is_empty():
                        print("Pila vacía")
                        continue
                    else:
                        pila.imprimir()
                    esperar_usuario()

                case 7:
                    print("Saliendo del editor...")
                    esperar_usuario()
                    break

                case _:
                    print("Opción no válida, intente de nuevo")
                    esperar_usuario()

        except ValueError:
            print("Error: Ingrese un valor numérico válido para la posición")
            esperar_usuario()
        except IndexError:
            print("Error: Posición fuera de rango")
            esperar_usuario()
        except Exception as e:
            print(f"Error inesperado: {e}")
            esperar_usuario()
    
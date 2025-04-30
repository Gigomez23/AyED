"""
funciones.py

Este modulo contiene las funciones generales para el editor de texto.

Funciones:
    limpiar_consola: Limpia la consola dependiendo del sistema operativo.
    esperar_usuario: Espera a que el usuario presione Enter para continuar.
    mostrar_menu: Muestra el menú principal del editor de texto y devuelve la opción seleccionada por el usuario.
"""

import os
import platform

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


def mostrar_menu(texto_actual):
    """Muestra el menú principal del editor de texto y devuelve la opción seleccionada por el usuario."""
    print("\n--- Editor de Texto ---")
    if not texto_actual:
        print("")
    else:        
        print(texto_actual)
    print("1. Insertar texto")
    print("2. Borrar texto")
    print("3. Copiar texto")
    print("4. Pegar texto")
    print("5. Deshacer")
    print("6. Rehacer")
    print("7. Mostrar estado actual")
    print("8. Salir")
    return int(input("Seleccione una opción: "))
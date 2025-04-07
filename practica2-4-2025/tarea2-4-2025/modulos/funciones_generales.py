import os

def clear_screen():
    """Funcion para limpiar la pantalla."""
    os.system('cls' if os.name == 'nt' else 'clear')

def limpiar():
    """Funcion para limpiar la pantalla despues de interaccion de usuario"""
    input("Presione Enter para continuar...")
    clear_screen()

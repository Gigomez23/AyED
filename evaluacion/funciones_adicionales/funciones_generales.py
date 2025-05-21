import os, platform

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
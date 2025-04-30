"""
problema4.py

Este archivo contiene la funcion main y sirve como punto de entrada para el editor de texto.

Autores: Andrea Bojorge
         Gabriel Gomez
         Gabriel Lacayo
         Yaritza Diaz
"""

from funciones import *
from models import EditorTexto

def main():
    """Funcion principal que ejecuta el editor de texto.
    Esta funcion inicializa el editor de texto y muestra un menu con las opciones disponibles.
    """
    editor = EditorTexto()

    while True:
        opcion = mostrar_menu(editor.texto)

        try:
            match opcion:
                case 1:
                    texto = input("Texto a insertar: ")
                    pos = int(input("Posición para insertar: "))
                    editor.agregar_accion('insertar', texto, pos-1)
                    esperar_usuario()

                case 2:
                    if not editor.texto:
                        print("No hay texto para borrar")
                        continue

                    print(f"Texto actual: '{editor.texto}'")
                    pos = int(input("Posición para borrar: "))
                    inicio = pos - 1
                    longitud = int(input("Cantidad de caracteres a borrar: "))
                    texto_borrado = editor.texto[inicio:inicio + longitud]
                    editor.agregar_accion('borrar', texto_borrado, inicio)
                    esperar_usuario()

                case 3:
                    if not editor.texto:
                        print("No hay texto para copiar")
                        continue

                    print(f"Texto actual: '{editor.texto}'")
                    pos = int(input("Posición inicial para copiar: "))
                    inicio = pos - 1
                    longitud = int(input("Cantidad de caracteres a copiar: "))
                    texto_copiado = editor.texto[inicio:inicio + longitud]
                    editor.agregar_accion('copiar', texto_copiado, inicio)
                    print(f"Texto copiado al portapapeles: '{texto_copiado}'")
                    esperar_usuario()

                case 4:
                    if not editor.portapapeles:
                        print("Clipboard vacío")
                        continue

                    pos = int(input("Posición para pegar: "))
                    editor.agregar_accion('pegar', editor.portapapeles, pos-1)
                    print(f"Texto pegado: '{editor.portapapeles}'")
                    esperar_usuario()

                case 5:
                    accion = editor.deshacer()
                    if accion:
                        print(f"Deshecho: {accion}")
                        esperar_usuario()
                    else:
                        print("No hay acciones para deshacer")
                        esperar_usuario()

                case 6:
                    accion = editor.rehacer()
                    if accion:
                        print(f"Rehecho: {accion}")
                        esperar_usuario()
                    else:
                        print("No hay acciones para rehacer")
                        esperar_usuario()

                case 7:
                    editor.mostrar_estado()
                    esperar_usuario()

                case 8:
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


#punto de partida del programa
if __name__ == "__main__":
    main()


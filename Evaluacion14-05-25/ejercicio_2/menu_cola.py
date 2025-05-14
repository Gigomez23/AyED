from cola import Documento, ColaImpresion

def mostrar_menu():
    print("\n--- Menú Cola de Impresión ---")
    print("1. Agregar documento a la cola")
    print("2. Procesar siguiente documento")
    print("3. Mostrar documento que se está imprimiendo actualmente")
    print("4. Salir")

def main():
    cola = ColaImpresion()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del documento: ")
            while True:
                usuario = input("Ingrese el nombre del usuario: ")
                if usuario.isalpha():
                    break
                else:
                    print("El nombre de usuario solo debe contener letras. Intente de nuevo.")
            while True:
                try:
                    num_paginas = int(input("Ingrese el número de páginas: "))
                    if num_paginas <= 0:
                        print("El número de páginas debe ser mayor que cero.")
                        continue
                    break
                except ValueError:
                    print("Por favor, ingrese un número válido.")
            doc = Documento(nombre, usuario, num_paginas)
            cola.agregar_documento(doc)

        elif opcion == "2":
            documento_impreso = cola.procesar_siguiente()
            if documento_impreso:
                print(f"Documento procesado (impreso): {documento_impreso}")
                siguiente = cola.documento_actual()
                print("No hay más documentos en la cola para imprimir.")
            else:
                print("No hay documentos para procesar.")

        elif opcion == "3":
            actual = cola.documento_actual()
            if actual:
                print(f"Documento que se está imprimiendo actualmente: {actual}")
            else:
                print("No hay documentos en la cola para imprimir.")

        elif opcion == "4":
            print("Saliendo del sistema de cola de impresión.")
            break

        else:
            print("Opción no válida. Por favor, seleccione una opción del menú.")

if __name__ == "__main__":
    main()

from clases import *

def agregar_valor(ListaEnlazada: ListaEnlazada):
    """
    Agrega un nuevo valor a la lista enlazada.
    """
    valor = int(input("Ingrese el valor a agregar: "))
    ListaEnlazada.insertar(valor)
    print(f"Valor {valor} agregado a la lista.")


def menu(ListaEnlazada: ListaEnlazada):
    """
    Muestra el menú de opciones y ejecuta la opción seleccionada.
    """
    while True:
        print("\nMenu:")
        print("1. Agregar valor al inicio")
        print("2. Mostrar lista")
        print("3. Buscar valor")
        print("4. Eliminar valor")
        print("5. Salir")

        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            ListaEnlazada.insertar_inicio(ListaEnlazada)
        elif opcion == 2:
            ListaEnlazada.mostrar()
        elif opcion == 3:
            valor = int(input("Ingrese el valor a buscar: "))
            encontrado = ListaEnlazada.buscar(valor)
            if encontrado:
                print(f"Valor {valor} encontrado en la lista.")
            else:
                print(f"Valor {valor} no encontrado en la lista.")
        elif opcion == 4:
            valor = int(input("Ingrese el valor a eliminar: "))
            eliminado = ListaEnlazada.eliminar(valor)
            if eliminado:
                print(f"Valor {valor} eliminado de la lista.")
            else:
                print(f"Valor {valor} no encontrado en la lista.")
        elif opcion == 5:
            break
        else:
            print("Opción inválida, intente nuevamente.")
        print("6. Contar elementos")

if __name__ == "__main__":
    # Crear una instancia de la lista enlazada
    lista = ListaEnlazada()
    menu(lista)

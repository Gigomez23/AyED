from evaluacion.models.lista_enlazada import ListaEnlazada
from evaluacion.funciones_adicionales.funciones_generales import *

def agregar_valor(ListaEnlazada: ListaEnlazada):
    """
    Agrega un nuevo valor al final de la lista enlazada.
    """
    valor = int(input("Ingrese el valor a agregar: "))
    ListaEnlazada.insertar_final(valor)
    print(f"Valor {valor} agregado al final de la lista.")

def agregar_valor_inicio(ListaEnlazada: ListaEnlazada):
    """
    Agrega un nuevo valor al inicio de la lista enlazada.
    """
    valor = int(input("Ingrese el valor a agregar al inicio: "))
    ListaEnlazada.insertar_inicio(valor)
    print(f"Valor {valor} agregado al inicio de la lista.")

def mostrar_lista(ListaEnlazada: ListaEnlazada):
    """
    Muestra los valores de la lista enlazada.
    """
    ListaEnlazada.imprimir()

def buscar_valor(ListaEnlazada: ListaEnlazada):
    """
    Busca un valor en la lista enlazada.
    """
    valor = int(input("Ingrese el valor a buscar: "))
    encontrado = ListaEnlazada.buscar(valor)
    if encontrado:
        print(f"Valor {valor} encontrado en la lista.")
    else:
        print(f"Valor {valor} no encontrado en la lista.")

def eliminar_valor(ListaEnlazada: ListaEnlazada):
    """
    Elimina un valor de la lista enlazada.
    """
    valor = int(input("Ingrese el valor a eliminar: "))
    eliminado = ListaEnlazada.eliminar(valor)
    if eliminado:
        print(f"Valor {valor} eliminado de la lista.")
    else:
        print(f"Valor {valor} no encontrado en la lista.")

def contar_elementos(ListaEnlazada: ListaEnlazada):
    """
    Cuenta el número de elementos en la lista enlazada.
    """
    cantidad = ListaEnlazada.contar()
    print(f"La lista contiene {cantidad} elementos.")

def buscar_posicion_valor(ListaEnlazada: ListaEnlazada):
    """
    Busca la posición de un valor en la lista enlazada.
    """
    valor = int(input("Ingrese el valor para buscar su posición: "))
    posicion = ListaEnlazada.buscar_posicion(valor)
    if posicion != -1:
        print(f"El valor {valor} se encuentra en la posición {posicion}.")
    else:
        print(f"El valor {valor} no se encuentra en la lista.")

def menu5():
    """
    Muestra el menú de opciones y ejecuta la opción seleccionada.
    """
    listaEnlazada = ListaEnlazada()
    while True:
        print("\nMenu:")
        print("1. Agregar valor al final")
        print("2. Agregar valor al inicio")
        print("3. Mostrar lista")
        print("4. Eliminar valor")
        print("5. Contar elementos")
        print("6. Buscar posición de un valor")
        print("7. Salir")

        opcion = int(input("Seleccione una opción: "))

        match opcion:
            case 1:
                limpiar_consola()
                agregar_valor(listaEnlazada)
                esperar_usuario()
            case 2:
                agregar_valor_inicio(listaEnlazada)
                esperar_usuario()
            case 3:
                mostrar_lista(listaEnlazada)
                esperar_usuario()
            case 4:
                eliminar_valor(listaEnlazada)
                esperar_usuario()
            case 5:
                contar_elementos(listaEnlazada)
                esperar_usuario()
            case 6:
                buscar_posicion_valor(listaEnlazada)
                esperar_usuario()
            case 7:
                esperar_usuario()
                break
            case _:
                print("Opción inválida, intente nuevamente.")

if __name__ == "__main__":
    # Crear una instancia de la lista enlazada
    lista = ListaEnlazada()
    menu5()
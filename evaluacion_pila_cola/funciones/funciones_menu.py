from evaluacion_pila_cola.models.cola import Cola
from evaluacion_pila_cola.models.pila import Pila
from evaluacion_pila_cola.funciones.funciones_generales import *

def imprimir_menu():
    """
    Funciȯn para imprimir las opciones del menu
    """
    print("===Evaluaciȯn 26 de Mayo===")
    print("Seleccione una opciȯn:")
    print("1. Agregar Dato")
    print("2. Eliminar Dato")
    print("3. Organizar Dato")
    print("4. Salir")

def agregar_dato(Cola: Cola):
    entrada = input("Digite el dato para agregar a cola: ")
    Cola.insertar(entrada)
    esperar_usuario()


def eliminar_dato(Cola: Cola):
    Cola.eliminar()
    esperar_usuario()

def organizar_datos(Cola: Cola, Pila: Pila):
    lista_elementos = Cola.mostrar_valores()
    lista_temporales = [] #this can be a Cola instead?
    counter = 0
    for item in lista_elementos:
        if counter % 2 == 0:
            lista_temporales.append(item)
            Cola.eliminar()
            counter += 1
        else:
            Pila.push(item)
            Cola.eliminar()
            counter += 1

    for item in lista_temporales:
        Cola.insertar(item)
        print(f"Elemento {item} agregado a la cola.")

    Cola.imprimir()
    Pila.imprimir()
    esperar_usuario()








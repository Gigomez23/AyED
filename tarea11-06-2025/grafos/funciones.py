import os, platform
from models import Grafo

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
    """Imprime el menú principal del programa."""
    print("----- Menú Principal -----")
    print("1. Agregar arista")
    print("2. Imprimir grafo")
    print("3. Encontrar Vecinos de una vértice")
    print("4. Verificar conexiones entre dos aristas")
    print("5. Orden de recorrido BFS")
    print("6. Orden de recorrido DFS")
    print("7. Verificar si el grafo es conexo")
    print("8. Encontrar camino entre dos aristas")
    print("9. Salir")
    print("--------------------------")
    print("Seleccione una opción:")

def seleccion_tipo_grafo():
    """Solicita al usuario el tipo de grafo dirigido/no dirigido"""
    
    tipo = input("Seleccione el tipo de grafo (1 para no dirigido, 2 para dirigido): ")
    if tipo == "1":
        print("Ha seleccionado un grafo no dirigido.")
        esperar_usuario()
        return True
    elif tipo == "2":
        limpiar_consola()
        print("Ha seleccionado un grafo dirigido.")
        esperar_usuario()
        return False
    else:
        limpiar_consola()
        print("Selección no válida. Por favor, ingrese 1 o 2.")
        esperar_usuario()
        return seleccion_tipo_grafo()
    
def menu():
    """Función principal que ejecuta el menú del programa."""
    tipo = seleccion_tipo_grafo()
    grafo = None
    if tipo:
        grafo = Grafo()
    else:
        grafo = Grafo(es_dirigido=True)
    
    while True:
        imprimir_menu()
        try:
            opcion = int(input("Ingrese su opción: "))
        
            match opcion:
                case 1:
                    print("Ingrese los vértices de la arista (ingrese el primero, presione Enter e ingrese el segundo valor):")
                    vertice1 = input("Vértice 1: ")
                    vertice2 = input("Vértice 2: ")
                    grafo.agregar_arista(vertice1, vertice2)
                    print(f"Arista '{vertice1}' agregado con conexion a {vertice2}.")
                    esperar_usuario()
                
                case 2:
                    grafo.imprimir_grafo()
                    esperar_usuario()
                
                case 3:
                    arista = input("Ingrese el nombre del arista: ")
                    vecinos = grafo.obtener_vecinos(arista)
                    print(f"Vecinos de '{arista}': {vecinos}")
                    esperar_usuario()
                
                case 4:
                    arista1 = input("Ingrese el primer arista: ")
                    arista2 = input("Ingrese el segundo arista: ")
                    conexion = grafo.existe_arista(arista1, arista2)
                    print(f"¿Están conectados '{arista1}' y '{arista2}'? {'Sí' if conexion else 'No'}")
                    esperar_usuario()
                
                case 5:
                    inicio = input("Ingrese el vértice de inicio para BFS: ")
                    recorrido_bfs = grafo.bfs(inicio)
                    print(f"Orden de recorrido BFS desde '{inicio}': {recorrido_bfs}")
                    esperar_usuario()
                
                case 6:
                    inicio = input("Ingrese el vértice de inicio para DFS: ")
                    recorrido_dfs = grafo.dfs(inicio)
                    print(f"Orden de recorrido DFS desde '{inicio}': {recorrido_dfs}")
                    esperar_usuario()
                
                case 7:
                    es_conexo = grafo.es_conexo()
                    print(f"El grafo {'es conexo' if es_conexo else 'no es conexo'}.")
                    esperar_usuario()
                
                case 8:
                    inicio = input("Ingrese el vértice de inicio: ")
                    fin = input("Ingrese el vértice de destino: ")
                    camino = grafo.encontrar_camino(inicio, fin)
                    if camino:
                        print(f"Camino encontrado entre '{inicio}' y '{fin}': {' -> '.join(camino)}")
                    else:
                        print(f"No se encontró un camino entre '{inicio}' y '{fin}'.")
                    esperar_usuario()
                
                case 9:
                    print("Saliendo del programa...")
                    break
                
                case _:
                    print("Opción no válida. Por favor, intente de nuevo.")
                    esperar_usuario()
        except ValueError:
            print("Error: Entrada no válida. Por favor, ingrese un número entero.")
            esperar_usuario()
    

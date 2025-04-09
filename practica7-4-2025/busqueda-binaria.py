array_ejemplo = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


def bus_bin(lista, objetivo, izq, der):
    """Funcion que encuentra un objetivo en una lista ordenada usando busqeda binaria.
    La funcion recibe una lista, el objetivo a buscar, el indice izquierdo y el indice derecho.
    
    Args:
        lista (array): lista con datos de string
        objetivo (string): cadena objetiva
        izq (int): posicion de la izquierda de la lista
        der (int): posicion de la derecha de la lista

    Returns:
        int: valor de la posicion del objetivo en la lista
    """
    if izq > der:
        return -1  # No se encontro el objetivo
    med = (izq + der) // 2
    if lista[med] == objetivo:
        return med
    elif lista[med] < objetivo:
        return bus_bin(lista, objetivo, med + 1, der)
    else:
        return bus_bin(lista, objetivo, izq, med - 1)

if __name__ == "__main__":
    # Inicio del programa
    print("Array de letras: ", array_ejemplo)
    objetivo_usuario = input("Escribe la letra cuya posicion deseas encontrar: ").strip().lower()
    resultado = bus_bin(array_ejemplo, objetivo_usuario, 0, len(array_ejemplo) - 1)
    print(f"Letra encontrada en posicion: {resultado+1}")
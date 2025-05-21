from pila import Pila

def invertir_palabras(frase):
    pila = Pila()
    palabras = frase.split()

    # Apilar todas las palabras
    for palabra in palabras:
        pila.apilar(palabra)

    # Desapilar para invertir el orden
    invertida = []
    while not pila.esta_vacia():
        invertida.append(pila.desapilar())

    return ' '.join(invertida)

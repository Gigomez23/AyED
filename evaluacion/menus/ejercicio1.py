from evaluacion.funciones_adicionales.inversor import invertir_palabras

def menu1():
    frase = input("Introduce una frase: ")
    resultado = invertir_palabras(frase)
    print("Frase invertida:", resultado)

if __name__ == "__main__":
    menu1()

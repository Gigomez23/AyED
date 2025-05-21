from inversor import invertir_palabras

def main():
    frase = input("Introduce una frase: ")
    resultado = invertir_palabras(frase)
    print("Frase invertida:", resultado)

if __name__ == "__main__":
    main()

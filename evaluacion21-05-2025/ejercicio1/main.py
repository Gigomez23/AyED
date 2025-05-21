from conversor import infija_a_postfija
from evaluador import evaluar_postfija
from utilidades import contiene_letras

def menu():
    while True: 
        print("=== MENÚ ===")
        print("1. Convertir expresión infija a postfija")
        print("2. Convertir y evaluar expresión infija (numérica)")
        print("3. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            expresion = input("Introduce la expresión infija (con letras o números): ")
            postfija = infija_a_postfija(expresion)
            print("Expresión postfija:", postfija)

        elif opcion == '2':
            while True:
                expresion = input("Introduce la expresión infija (solo con números, sin variables): ")
                if contiene_letras(expresion):
                    print("Error: La expresión contiene letras. Solo se permiten números y operadores.")
                else:
                    break
            postfija = infija_a_postfija(expresion)
            print("Expresión postfija:", postfija)
            resultado = evaluar_postfija(postfija)
            print("Resultado:", resultado)

        elif opcion == '3':
            print("Saliendo del programa")
            break

        else:
            print("Opción inválida.")


if __name__ == '__main__':
    menu()
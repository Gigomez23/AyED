# Programa para convertir y evaluar expresiones aritméticas usando pilas

def prioridad(op):
    if op == '^':
        return 3
    if op in ('*', '/'):
        return 2
    if op in ('+', '-'):
        return 1
    return 0

def es_operador(c):
    return c in ['+', '-', '*', '/', '^']

def infija_a_postfija(exp):
    pila = []
    postfija = []
    for c in exp:
        if c == ' ':
            continue
        if c.isalnum():
            postfija.append(c)
        elif c == '(':
            pila.append(c)
        elif c == ')':
            while pila and pila[-1] != '(':
                postfija.append(pila.pop())
            if pila and pila[-1] == '(':
                pila.pop()
        else:
            while pila and prioridad(c) <= prioridad(pila[-1]):
                postfija.append(pila.pop())
            pila.append(c)
    while pila:
        postfija.append(pila.pop())
    return ''.join(postfija)

def evaluar_postfija(exp):
    pila = []
    for c in exp:
        if c.isdigit():
            pila.append(int(c))
        elif es_operador(c):
            b = pila.pop()
            a = pila.pop()
            if c == '+':
                pila.append(a + b)
            elif c == '-':
                pila.append(a - b)
            elif c == '*':
                pila.append(a * b)
            elif c == '/':
                pila.append(a // b)
            elif c == '^':
                pila.append(a ** b)
    return pila[0]

def contiene_letras(exp):
    return any(c.isalpha() for c in exp)

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
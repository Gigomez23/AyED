from utilidades import es_operador
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

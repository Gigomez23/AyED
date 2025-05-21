from utilidades import prioridad

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

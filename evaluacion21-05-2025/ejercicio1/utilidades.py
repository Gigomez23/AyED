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

def contiene_letras(exp):
    return any(c.isalpha() for c in exp)
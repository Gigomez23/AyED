from balance_checker import is_balanced

def main():
    test_cases = [
        ("()", True),
        ("({[]})", True),
        ("({[}])", False),
        ("(", False),
        ("", True),
        ("a + b - (c * d)", True)
    ]

    for expr, expected in test_cases:
        result = is_balanced(expr)
        print(f"Expresión: {expr:20} - Esperado: {expected} - Resultado: {result}")

if __name__ == "__main__":
    main()
#Ejemplificando funciones en Python
from modulos import *
activo = True

if __name__ == "__main__":
    while activo:
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Potencia")
        print("6. Salir")

        opcion = int(input("Digite su seleccion: "))
        match opcion:
            case 1:
                a = float(input("Ingrese el primer número: "))
                b = float(input("Ingrese el segundo número: "))
                resultado = suma(a, b)
                print(f"El resultado de la suma es: {resultado}")
                clear_function()
            case 2:
                a = float(input("Ingrese el primer número: "))
                b = float(input("Ingrese el segundo número: "))
                resultado = resta(a, b)
                print(f"El resultado de la resta es: {resultado}")
                clear_function()
            case 3:
                a = float(input("Ingrese el primer número: "))
                b = float(input("Ingrese el segundo número: "))
                resultado = multiplicacion(a, b)
                print(f"El resultado de la multiplicación es: {resultado}")
                clear_function()
            case 4:
                a = float(input("Ingrese el primer número: "))
                b = float(input("Ingrese el segundo número: "))
                try:
                    resultado = division(a, b)
                    print(f"El resultado de la división es: {resultado}")
                    clear_function()
                except ValueError as e:
                    print(e)
                    clear_function()
            case 5:
                a = float(input("Ingrese la base: "))
                b = float(input("Ingrese el exponente: "))
                resultado = potencia(a, b)
                print(f"El resultado de la potencia es: {resultado}")
                clear_function()
            case 6:
                activo = False
                print("Va a salir del programa....")
                clear_function()
        
import os
import platform

clear = None
if platform.system() == "Windows":
    clear = lambda: os.system('cls')
else:
    clear = lambda: os.system('clear')
text_ejemplo_5 = "Seleccione de que figura desea calcular la superficie \n1. Cuadrado \n2. Círculo \n3. Rectángulo \n4. Trapecio \n5. Triángulo \n0. Salir"
text = "Seleccione un tipo de vehiculo: \n 1. Bicicleta \n 2. Moto \n 3. Carro \n 4. Camión \n 0. Salir"
text_main = "Seleccione que ejercisio desea revisar \n1. Importe Vehiculos \n2. Facturación \n3. Venta Docenas \n4. Cifras Númericas \n5. Cálculo Superficies \n0. Cerrar Programa"
active = True

def define(num, distance, ton):
    match num:
        case 1: 
            return 100
        case 2: 
            return 30 * distance
        case 3: 
            return (30 * distance) + (25 * ton)

def clear_function():
    input("Presione cualquier tecla para borrar y continuar....")
    clear()

def calculo_vehiculo():
    active_vehiculo = True
    while active_vehiculo:
        print(text)
        seleccion = int(input("Digite el número correspondiente al vehiculo: "))
        if seleccion == 1:
            print(define(1, 0, 0))
            input("Presione cualquier tecla para continuar y limpiar la consola...")
            clear()
        elif seleccion == 2 or seleccion==3:
            distance = int(input("Digite distancia recorrida: "))
            print(define(2, distance, 0))
            input("Presione cualquier tecla para continuar y limpiar la consola...")
            clear()
        elif seleccion == 4:
            distance2 = int(input("Digite distancia recorrida: "))
            weight = int(input("Digite el peso del camión: "))
            print(define(3, distance2, weight))
            input("Presione cualquier tecla para continuar y limpiar la consola...")
            clear()
        elif seleccion == 0:
            active_vehiculo = False
            input("Presione cualquier tecla para continuar y limpiar la consola...")
            clear()
            print("Programa terminado de forma exitosa.")

def facturacion():
    compra = float(input("Ingrese el subtotal de la compra C$: "))
    if compra > 1000:
        subtotal = (compra - (compra * 0.12))
        print(f"Total a facturar: C$ {(subtotal - (subtotal * 0.15))}")
    else:
        print(f"Total a facturar: C$ {(compra + (compra * 0.15))}")
    clear_function()
    
def por_mayor():
    cantidad_cajas = int(input("Digite la cantidad de docenas a comprar: "))
    precio_cajas = int(input("Digite el precio por docena: C$"))
    subtotal_cajas = cantidad_cajas * precio_cajas
    if (cantidad_cajas > 3):
        total = subtotal_cajas - (subtotal_cajas * 0.15)
        cantidad_productos = cantidad_cajas - 3
        print(f"Precio original: C${subtotal_cajas} \nTotal con descuento aplicado (15%) C${total}. \nDe regalía recibe {cantidad_productos} unidades adicionales")
    else:
        total_menor = subtotal_cajas - (subtotal_cajas * 0.1)
        print(f"Precio original: C$ {subtotal_cajas} \nTotal con descuento aplicado (10%) C${total_menor}.")
    clear_function()
        
    

def igual_al_reves():
    numero = input("Ingrese el numero: ")
    numero_lista = list(numero.replace(" ", ""))
    numero_reves = ""
    largo = int(len(numero_lista))
    for i in reversed(range(0, largo)):
        numero_reves += numero_lista[i]
    print(numero_reves)
    if numero_reves == numero:
        print(f"{numero} (numero original) es igual a {numero_reves} (número al revés).")
    else:
        print(f"Los números {numero} y su reversa {numero_reves} no son igual")
    clear_function()

def calculo_superficie():
    active_local = True
    while active_local:
        print(text_ejemplo_5)
        seleccion = int(input("Digite la selección: "))
        match(seleccion):
            case 1:
                clear()
                print("Calculo de area de Cuadrado. ")
                lado = int(input("Digite la distancia del lado: "))
                print(f"El area del cuadrado es de: {lado*lado}")
            case 2:
                clear()
                print("Calculo de area de Circulo. ")
                radio = int(input("Digite la distancia del radio: "))
                print(f"El area del cuadrado es de: {radio*radio*3.14159}")
            case 3:
                clear()
                print("Calculo de area de Rectángulo. ")
                base = int(input("Digite la base del rectangulo: "))
                altura = int(input("Digite la altura del rectangulo: "))
                print(f"El area del rectángulo es de {base*altura}")
            case 4:
                clear()
                print("Calculo de area de Trapecio. ")
                base1 = int(input("Digite la distancia de la primera base: "))
                base2 = int(input("Digite la distancia de la segunda base: "))
                altura_trap = int(input("Digite la altura: "))
                print(f"El área del trapecio es de {(base1+base2)*(altura/2)}")
            case 5:
                clear()
                print("Calculo de area de Triangulo. ")
                base_triangulo = int(input("Digite la distancia de la base: "))
                altura_triangulo = int(input("Digite la distancia de la altura: "))
                print(f"El área del triangulo es de {(base_triangulo*altura_triangulo)/2}")
            case 0:
                print("Va a salir de calculadora de superficie")
                active_local = False
        clear_function()
                
while active:
    print(text_main)
    seleccion_usuario = int(input("Digite su selección: "))
    match(seleccion_usuario):
        case 1:
            clear()
            calculo_vehiculo()
        case 2:
            clear()
            facturacion()
        case 3:
            clear()
            por_mayor()
        case 4:
            clear()
            igual_al_reves()
        case 5:
            clear()
            calculo_superficie()
        case 0:
            print("va a salir del programa")
            clear_function()
            active = False
                

                

    
        
from modulos.funciones_generales import *

class Inventario:
    def __init__(self):
        self.articulos = []
        
    def agregar_inventario(self, articulo):
        self.articulos.append(articulo)
        print(f"Se ha agregado el producto {articulo.nombre} al inventario.")
        
    
    def mostrar_inventario(self):
        if not self.articulos:
            print("El inventario está vacío.")
        else:
            for articulo in self.articulos:
                print(f"Codigo: {articulo.codigo}, Nombre: {articulo.nombre}, Precio: {articulo.precio}, Stock: {articulo.cantidad}")
                
    def modificar_articulo(self):
        if not self.articulos:
            print("El inventario está vacío.")
            
        else:
            print("Modificar articulo")
            print("Selecciona el articulo a modificar:")
            i = 1
            for articulo in self.articulos:
                print(f"{i}. {articulo.nombre}, {articulo.codigo}")
                i += 1
            seleccion = int(input("Selecciona el articulo a modificar: "))
            articulo_modificar = self.articulos[seleccion - 1]
            clear_screen()
            print("¿Qué deseas modificar?")
            print("Articulo: ", articulo_modificar.nombre)
            print("1. Stock\n2. Precio\n3. Nombre\n4. Codigo\n")
            seleccion_modificar = int(input("Selecciona la opción: "))
            match seleccion_modificar:
                case 1:
                    articulo_modificar.modificar_stock()
                case 2:
                    articulo_modificar.modificar_precio()
                case 3:
                    articulo_modificar.modificar_nombre()
                case 4:
                    articulo_modificar.modificar_codigo()
                case _:
                    print("Opción no válida.")
    
    def ver_datos_de_producto(self):
        if not self.articulos:
            print("El inventario está vacío.")
            
        else:
            print("Modificar articulo")
            print("Selecciona el articulo a revisar:")
            for articulo in self.articulos:
                i = 1
                print(f"{i}. {articulo.nombre}, {articulo.codigo}")
            seleccion = int(input("Selecciona el articulo a revisar: "))
            self.articulos[seleccion-1].mostrar_informacion()
    
            
        
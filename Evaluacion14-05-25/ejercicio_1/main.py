from cola import Cola

def mostrar_menu():
    print("\n--- Sistema de Cola de Atención Clínica ---")
    print("1. Agregar paciente a la cola")
    print("2. Atender siguiente paciente")
    print("3. Mostrar pacientes en espera")
    print("4. Salir")

def main():
    cola = Cola()
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            paciente = input("Ingrese el nombre del paciente: ")
            if paciente.isalpha() or (paciente.replace(' ', '').isalpha() and paciente.strip() != ''):
            
                cola.insertar(paciente)
            else:
                print("Error: El nombre del paciente debe contener solo letras y espacios.")
        elif opcion == "2":
            cola.eliminar()
        elif opcion == "3":
            cola.imprimir()
        elif opcion == "4":
            print("Saliendo del sistema")
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")

if __name__ == "__main__":
    main()

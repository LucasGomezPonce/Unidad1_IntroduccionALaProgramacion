"""
1 - Escribe un programa que administre el inventario de una tienda.
El programa debe permitir agregar nuevos productos, actualizar las cantidades de los productos existentes, y mostrar e inventario actual
2 - Escribe un programa que permita llevar un registro de las calificaciones de varios estudiantes, actualizar las calificaciones de un estudiante existente y mostra el promedio de calificaciones de un estudiante especifico"""

# Diccionario para almacenar el inventario
inventario = {}

# Función para agregar o actualizar productos


def administrar_inventario():

    inventario = {}

    while True:
        print("""
              .:MENU:.
1 - Agregar nuevo producto
2 - Mostrar inventario 
3 - Salir""")
        op = int(input("Ingresa la opcion: "))

        if op == 1:
            producto = input("Agregar producto: ")
            cantidad = input("Agrega la cantidad: ")

            if producto in inventario:
                inventario[producto] += cantidad

            else:
                inventario[producto] = cantidad

        if op == 2:
            print('Inventario')
            for prod in inventario.keys():
                print(f"{prod}: {inventario[prod]}")
        else:
            break


administrar_inventario()

# Diccionario para almacenar las calificaciones de los estudiantes
calificaciones = {}

# Función para administrar el registro de calificaciones


def administrar_calificaciones():
    while True:
        print("\nOpciones:")
        print("1. Agregar o actualizar calificaciones de un estudiante")
        print("2. Mostrar promedio de un estudiante")
        print("3. Mostrar todos los estudiantes y sus calificaciones")
        print("4. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            estudiante = input("Nombre del estudiante: ")
            calif = float(input("Nueva calificación: "))

            # Agregar o actualizar las calificaciones
            if estudiante in calificaciones:
                calificaciones[estudiante].append(calif)
                print(f"Calificación agregada para {estudiante}.")
            else:
                calificaciones[estudiante] = [calif]
                print(
                    f"Estudiante {estudiante} agregado con su primera calificación.")

        elif opcion == "2":
            estudiante = input("Nombre del estudiante: ")
            if estudiante in calificaciones:
                promedio = sum(
                    calificaciones[estudiante]) / len(calificaciones[estudiante])
                print(f"El promedio de {estudiante} es {promedio:.2f}.")
            else:
                print(f"{estudiante} no está registrado.")

        elif opcion == "3":
            print("\nRegistro de calificaciones:")
            for estudiante, califs in calificaciones.items():
                print(f"{estudiante}: {califs}")

        elif opcion == "4":
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida. Intenta nuevamente.")


administrar_calificaciones()

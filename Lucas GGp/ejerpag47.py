"""
1- Escribe un programa que solicite tres lados de un triangulo e indique si es equilatero, isoceles o escaleno
"""

lado1 = int(input("Ingrese el lado 1: "))
lado2 = int(input("Ingrese el lado 2: "))
lado3 = int(input("Ingrese el lado 3: "))

if lado1 == lado2 and lado1 == lado3:
    print("El triangulo es equilatero")
elif lado1 != lado2 and lado1 != lado3 and lado2 != lado3:
    print("El triangulo es Escaleno")
else:
    print("El triangulo es isoceles")

"""Escribe un programa que solicite al usuario que ingrese una contrasea y confirme la contraseña. El programa debe verificar si ambas contraseñas coinciden y no estan vacias"""

contra = input("Ingrese una contraseña: ")
contraConfirm = input("Confime la contraseña: ")

if contra == contraConfirm:
    print("Las contraseñas coinciden")
else:
    print("Las contraseñas no coinciden")

"""Escribe un programa que solicite al usuario el precio y la cantidad de un producto. Clasifique el producto como "caro" si el precio es mayor a $100 o si la cantidad es menor a 10 y el precio es mayor a $50, de lo contrario, clasifiquelo como "barato" Incluye condiciones para manejar valores falsos(0 o vacio)"""


precio = int(input("Ingrese el precio de un producto: "))
cantidad = int(input("ingrese la cantidad: "))

if precio <= 0:
    print("Error, el precio debe ser mayor a cero")
else:
    if precio > 100 or cantidad < 10 and precio > 50:
        print("El producto esta clasificado como Caro")
    else:
        print("El producto esta clasificado como Barato")


"""Escribe un programa que solicite al usuario su nombre, edad y numero de telefono. Verificar que ninguno de estos datos este vacio o sea un valor falso"""

nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
telefono = int(input("ingrese su telefono: "))

if len(nombre) < 1:
    print(f"Nombre ingresado no valido {nombre}")
if edad < 1 and edad > 100:
    print("Edad no valida")
telefonoStr = str(telefono)
if len(telefonoStr) < 9:
    print("Telefono mal ingresado")

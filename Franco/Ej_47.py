
#1. Escribe un programa que solicite tres lados de un triángulo e indique si es equilátero, isósceles o escaleno.

lado_1 = int(input("Ingrese el lado 1 del triangulo: "))

lado_2 = int(input("Ingrese el lado 2 del triangulo: "))

lado_3 = int(input("Ingrese el lado 3 del triangulo: "))

if lado_1 == lado_2 and lado_2 == lado_3 :
    print("Este triangulo es equilatero ")

elif lado_1 == lado_2 and lado_2 != lado_3 or lado_1 == lado_3 and lado_3 != lado_2 or lado_2 == lado_3 and lado_3 != lado_1 :
    print("Este triangulo es isósceles ")
     
else: 
    print("Este triangulo es escaleno ")

# 2. Escribe un programa que solicite al usuario que ingrese una
#contraseña y confirme la contraseña. El programa debe verificar si
#ambas contraseñas coinciden y no están vacías.

contraseña = str(input("Ingrese su contraseña: "))

confirme = str(input("Confirme su contraseña: "))

if contraseña == confirme:
    print("Ambas contraseñas coinciden ")

else: 
    print("Intente nuevamente")    

#3. Escribe un programa que solicite al usuario el precio y la cantidad
#de un producto. Clasifique el producto como "caro" si el precio es
#mayor de $100 o si la cantidad es menor que 10 y el precio es
#mayor de $50. De lo contrario, clasifíquelo como "barato". Incluye
#condiciones para manejar valores falsos (0 o vacío).

precio = int(input("Ingrese un precio del producto : "))

cant = int(input("Ingrese la cantidad del producto: "))

if precio <= 0 and cant <= 0 :
    print("ERROR INTENTE NUEVAMENTE. (Espacios vacios) ")

elif precio > 100 or precio > 50 and cant < 10:
    print("El producto es caro. ")

else: 
    print("El producto es barato. ")


#4. Escribe un programa que solicite al usuario su nombre, edad y
#número de teléfono. Verifica que ninguno de estos datos esté vacío
#o sea un valor falso (por ejemplo, 0)

nombre = str(input("Ingrese su nombre: "))
edad = int(input("Ingrese su edad: "))
numero_telefono = int(input("Ingrese su numero de telefono: "))

if  nombre != None and nombre != 0 and edad > 0 and numero_telefono != None and numero_telefono !=0 :
    print("Los datos son correctos ")
else: 
    print("Los datos no son correctos")

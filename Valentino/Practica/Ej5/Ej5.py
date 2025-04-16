""" Escribe un programa que a partir de un nuemro entero 
positivo, muestre por pantalla si es primo o no. """

try: 
    numero = int(input("Ingrese un numero: "))

    if numero % 2 == 0:
        print(f"El numero ingresado: {numero} es par")
    else:
       print(f"el numero ingresado: {numero} es impar")
except ValueError:
    print("Por favor, ingrese un numero valido")


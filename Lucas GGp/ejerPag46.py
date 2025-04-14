"""
1- Escribe un programa que a partir de un numero entero positivo, muestre por pantalla si es par o impar
2- Escribe un programa que a partir de un nuemro entero positivo, muestre por pantalla si es primo o no.
3- Escribe un programa que permita realizar la division de dos numeros siempre y cuando el denominador sea 0

"""

# Ejer 01

numero = int(input("Ingrese un numero entero positivo: "))

if numero % 2 == 0:
    print(f"El numero {numero} es par")
else:
    print(f"El numero {numero} es impar")

# Ejer 02

countDiv = 0

for div in range(1, numero):
    if numero % div == 0:
        countDiv += 1


if countDiv <= 1:
    print(f"El numero {numero} es primo")
else:
    print(f"El numero no {numero} es primo")

# Ejer 03
numeroDenominador = int(input("Ingrese un numero distinto a cero: "))

if numeroDenominador != 0:
    div = numero / numeroDenominador
    print(
        f"El resultado de la division entre {numero} y {numeroDenominador} es {div}")
else:
    print("No se puede dividir por cero")

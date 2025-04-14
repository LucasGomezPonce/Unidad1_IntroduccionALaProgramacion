"""Modifica el siguiente codigo (que identifica el mayor de dos numeros) a fin de encontrar ahora el mayor de 3 numeros."""

# numero_1 = 12
# numero_2 = -5

# if numero_1 > numero_2:
#     print(f"El mayor de los dos numeros es {numero_1}")
# else:
#     print(f"El mayor de los dos numeros es {numero_1}")


num1 = int(input('Ingrese un numero: '))
num2 = int(input('Ingrese un numero: '))
num3 = int(input('Ingrese un numero: '))


if num1 >= num2 and num1 >= num3:
    print(f"El mayor de los 3 numeros es {num1}")
elif num2 >= num1 and num2 >= num3:
    print(f"El mayor de los 3 numeros es {num2}")
else:
    print(f"El mayor de los 3 numeros es {num3}")

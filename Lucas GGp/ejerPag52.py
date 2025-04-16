"""
1- Escribe un programa que sume todos los numeros de una lista y luego responde. Que tipo de variable utilizamos para resolver?

Respuesta, usamos la variable acumuladora "suma_total"
"""

lista = [5, 2, 3, 4, 8]
suma_total = 0
for num in lista:
    suma_total += num

print(f"La suma total de todos los elementos de la lista es {suma_total}")

"""Escribe un programa que imprima el cuadrado de los numeors del 1 al 10"""

for num in range(1, 11):
    print(f"{num} al cuadrado es = {num**2}")

"""Escribe un programa que cuente los caracteres de una cadena de texto proporcionada por el usuario utilizando un for"""

cadena = input("Ingrese una cadena de texto: ")

contador = 0
for caracter in cadena:
    contador += 1
print(f"La cadena: {cadena} tiene {contador} caracteres")

"""Escribe un programa que cuente el numero de vocales en una cadena de texto proporcionada por el usuario"""

vocales = "aeiouAEIOU"

cadena = input("Ingrese una cadena de texto para contar sus vocales: ")

contadorVocales = 0
for caracter in cadena:
    if caracter in vocales:
        contadorVocales += 1

print(
    f"La cantidad de vocales que tiene la cadena {cadena} es {contadorVocales}")

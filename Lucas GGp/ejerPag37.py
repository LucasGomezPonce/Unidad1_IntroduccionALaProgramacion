"""
Modulo programador - Eje1 Python introduccion pagina 35, en pdf pagina 37
1- Escribe un programa que pida al usuario el radio de un circulo y calcule el area
2- Escribe un programa que convierta una temperatura dada en grados Celcius a grados Fahrenheit.
3- Escribe un programa que pida al usuario los dos catetos de un triangulo y calcule la hipotenusa
4- Escribe un programa que pida al usuario su año de nacimiento, calcule su edad y genere un mensaje de saludo personalizado que incluya su nombre y la edad calculada.
"""
# # Ejer 01
from datetime import datetime
from ast import If
import math

radio = int(input('Ingresa el radio de un circulo: '))

area = math.pi * ((radio)**2)

print(area)

# Ejer 02

gradosCel = int(input("Ingrese la temperatura en grados Celcius: "))

gradosFahr = (gradosCel*(9/5)+32)
print(f"{gradosCel}°C pasados a grados fahrenheit es {gradosFahr}°F")

# Ejer 03

catetoA = int(input("Ingresar cateto A: "))
catetoB = int(input("Ingresar cateto B: "))

hipotenusa = math.sqrt(catetoA**2 + catetoB**2)

print(
    f"Dados los catetos A={catetoA} y B={catetoB} la hipotenusa es {hipotenusa}")

# Ejer 04


fecha_actual = datetime.now()

anioActual = int(fecha_actual.year)
mesActual = int(fecha_actual.month)
diaActual = int(fecha_actual.day)


dia = int(input('Ingrese dia de nacimiento: '))
mes = int(input('Ingrese mes de nacimiento: '))
anio = int(input('Ingrese año de nacimiento: '))
nombre = input('Ingrese su nombre: ')

edad = 0

edad = anioActual - anio

if mesActual < mes or (mesActual == mes and diaActual < dia):
    edad -= 1

print(f"Hola {nombre}, tienes {edad} de edad")

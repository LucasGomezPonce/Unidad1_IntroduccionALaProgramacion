"""
Modulo programador - Eje1 Python introduccion pagina 35, en pdf pagina 37
1- Escribe un programa que pida al usuario el radio de un circulo y calcule el area
2- Escribe un programa que convierta una temperatura dada en grados Celcius a grados Fahrenheit.
3- Escribe un programa que pida al usuario los dos catetos de un triangulo y calcule la hipotenusa
4- Escribe un programa que pida al usuario su año de nacimiento, calcule su edad y genere un mensaje de saludo personalizado que incluya su nomvre y la edad calculada.
"""

import math

radio = int(input('Ingresa el radio de un circulo: '))

area = math.pi * ((radio)**2)

print(area)

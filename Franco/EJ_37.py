
#1- Escribe un programa que pida al usuario el radio de un circulo y calcule el area

radio_circulo = int(input("Ingrese el radio de un circulo: "))

area = 3.14 * radio_circulo**2

print(f"El area del circulo es {area}")


#2- Escribe un programa que convierta una temperatura dada en grados Celcius a grados Fahrenheit.

grados_celcius = float(input("Ingrese la temperatura actual en grados celsius: "))

grados_fahrenheit = grados_celcius * 9 / 5 + 32

print(f"La temperatura actual es: {grados_fahrenheit}F  ")


# 3- Escribe un programa que pida al usuario los dos catetos de un triangulo y calcule la hipotenusa

cateto_a = float(input("Ingrese el cateto A: "))

cateto_b = float(input("Ingrese el cateto B: "))

hipotenusa = ( cateto_a **2 + cateto_b **2 ) ** (1/2)

print(f"La hipotenusa del triangulo es: {hipotenusa} ")


#4- Escribe un programa que pida al usuario su año de nacimiento, calcule su edad y genere un mensaje de saludo personalizado que incluya su nombre y la edad calculada.

fecha_nacimiento = int(input("Ingrese su fecha de nacimiento: "))

edad = 2025 - fecha_nacimiento

nombre = input("Ingrese su nombre: ")

print(f"Buenos dias {nombre} su edad es {edad}")
"""Modifica el siguiente codigo (que identifica el mayor de dos numeros) a fin de encontrar ahora el mayor de 3 numeros."""

# numero_1 = 12
# numero_2 = -5

# if numero_1 > numero_2:
#     print(f"El mayor de los dos numeros es {numero_1}")
# else:
#     print(f"El mayor de los dos numeros es {numero_1}")

numero_1 = 12
numero_2 = 5 
numero_3 = 80 

if numero_1 > numero_2 and numero_1 > numero_3:
    print(f"El mayor de los tres numeros es: {numero_1}")

elif numero_2 > numero_1 and numero_2 > numero_3:
    print(f"El mayor de los tres numeros es: {numero_2}")

else: 
    print(f"El mayor de los tres numeros es: {numero_3}")

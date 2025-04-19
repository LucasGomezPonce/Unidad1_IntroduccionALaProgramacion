"""Escribe un programa que genere un numero aleatorio del 1 al 100 y permita al usurio adivinar el numero, El programa debe brindar pistas (ej. el numero secreto es mayor) y debe continuar pidiendo al usuario que adivine hasta que acierte. Al finalizar, debe mostrar el numero de intentos"""


import random


numeroAleatorio = random.randint(1, 100)
intento = 0
while True:
    num = int(input("Adivine el numero del 1 al 100: "))

    intento += 1
    if num == numeroAleatorio:
        print(f"Numero acertado '{numeroAleatorio}' en {intento} intentos")
        break
    if numeroAleatorio < num:
        print(f"El numero es menor a {num}")
    else:
        print(f"El numero es mayor a {num}")

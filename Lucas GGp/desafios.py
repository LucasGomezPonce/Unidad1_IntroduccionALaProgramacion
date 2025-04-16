"""Escribe un programa que pida a usuario un entero de tre digitos y entregue el numero con los digitos en orden inverso"""


def desafio01():
    numero = int(input("ingresa un numero de 3 digitos"))

    numeroACopiar = 0
    if len(str(numero)) != 3:
        print("Error, debe ingresar un numero de 3 digitos.")
        return

    while numero > 0:
        numeroACopiar = (numeroACopiar*10) + numero % 10
        numero = numero // 10
    print(numeroACopiar)


def desafio02():

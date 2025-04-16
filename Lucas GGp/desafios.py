"""Escribe un programa que pida a usuario un entero de tre digitos y entregue el numero con los digitos en orden inverso"""


import math


def desafio01():
    numero = int(input("ingresa un numero de 3 digitos: "))

    numeroACopiar = 0
    if len(str(numero)) != 3:
        print("Error, debe ingresar un numero de 3 digitos.")
        return

    while numero > 0:
        numeroACopiar = (numeroACopiar*10) + numero % 10
        numero = numero // 10
    print(numeroACopiar)


"""Escriba un programa que pregunte al usuario la hora actual t  del reoj y un numeor entero de horas h, que indique que hora marcara el reloj dentro de h horas"""


def desafio02():
    t = int(input("Ingrese la hora actual: "))
    if t <= 23 and t >= 0:
        h = int(input("Ingrese la cantidad de horas: "))

        horaFinal = (t + h) % 24
        print(horaFinal)
    else:
        print("Error, formato de hora invalido")


"""Escribe un programa que pida al usuario un  numero entero y muestre por pantalla si es un numero primo o no"""


def desafio03():
    numero = int(input("Ingrese un numero: "))

    if numero > 1:
        numeroReduc = int(math.sqrt(numero))
        contador = 0

        for i in range(2, numeroReduc):
            resto = numero % i

            print(f"{numero} % {i} = {resto}")

            if resto == 0:
                contador += 1
                print(f"El {numero} No es numero primo")
                break
        else:
            print(f"El {numero} es numero primo")


def desafio04():
    pass

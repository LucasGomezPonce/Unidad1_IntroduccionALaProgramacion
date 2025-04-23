""" Escriba un programa que pida al usuario un entero de tres dígitos, y entregue el número con
los dígitos en orden inverso: """

def funcion():
    numero = int(input("Ingrese un numero de 3 digitos: "))

    numeroACopiar = 0 
    if len(str(numero)) != 3:
        print("Error | Debe ingresar un numero de 3 digitos")
        return
    
    while numero > 0:
         numeroACopiar = (numeroACopiar*10) + numero % 10
         numero = numero // 10
    print(numeroACopiar)
    
funcion()
         

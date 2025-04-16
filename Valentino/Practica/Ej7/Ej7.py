""" Escribe un programa que permita realizar la division de dos 
numeros siempre y cuando el denominador sea 0"""

numero1 = int(input("ingrese el primer numero: "))
numero2 = int(input("Ingrese el segundo numero: "))

#!= 0 

if numero2 == 0:    
    print("Error | El denominador no puede ser 0")
else: 
    division = numero1 / numero2
    print(f"El resultado de la division es: {division}")



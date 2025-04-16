
#1- Escribe un programa que a partir de un numero entero positivo, muestre por pantalla si es par o impar


numero = int(input("Ingrese un numero: "))

par = numero % 2

if par == 0 :
    print("El numero ingresado es par")

else:
    print("El numero ingresado es inpar")    



#3- Escribe un programa que permita realizar la division de dos numeros siempre y cuando el denominador no sea 0
 
dividendo = int(input("Ingrese un numero que desee dividir: "))

divisor = int(input("Ingrese el numero divisor: "))

if not divisor == 0 :
    cociente = dividendo / divisor
    print(f"El resultado es {cociente}")

else:
    print("El ejercicio no puede resolverse")    







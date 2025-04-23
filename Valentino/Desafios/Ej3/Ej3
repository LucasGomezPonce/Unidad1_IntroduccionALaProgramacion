""" Escribe un programa que a partir de un nuemro entero 
positivo, muestre por pantalla si es primo o no. """

numero = int(input("Ingrese un numero: "))

if numero > 1:

    contador=0

    for i in range(2, numero):
        resto=numero%i 

        print(f"{numero} % {i} = {resto}")

        if resto == 0:
            contador+=1

    if contador == 0:

        print(f"El {numero} Es un numero primo") 
    else: 
        print (f"El {numero} No es numero primo")

else:

    print (f"El {numero} No es numero primo")


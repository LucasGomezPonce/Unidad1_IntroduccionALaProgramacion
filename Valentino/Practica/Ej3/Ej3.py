""" Escribe un programa que pida al usuario los dos catetos de un
triángulo rectángulo y calcule la hipotenusa. """

catetoA = float(input("Ingrese el primer cateto: "))
catetoB = float(input("Ingrese el segundo cateto: "))

hipotenusa = (catetoA ** 2 + catetoB ** 2) ** 0.5 


print (f"El resultado de la hipotenusa es: {hipotenusa}")
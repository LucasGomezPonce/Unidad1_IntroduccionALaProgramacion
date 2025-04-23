"""
1 -Crea una lista de numeros desordenados y ordenala en orden ascendente y descendente.
2 - Crea una lista de numeros que cuente el numero de veces que aparece el numero ingresado por el usuario.
3 - Crea una tupla con tres colores favoritos e imprime solo el segundo color.
4 - Crea una tupla de numeros y verifica si el numero ingresado por el usuario existe"""

listaDesord = [1, 8, 6, 7, 1, 3, 6]

listaDesord.sort()
listaDesord.reverse()
print(listaDesord)

num = int(input("Ingresa un numero para ver cuantas veces aparece en la lista: "))

count = listaDesord.count(num)
print(f"El numero {num} aparece {count} veces")

tuplaColores = ('Azul', 'Rojo', 'Verde')

print(f'El segundo color de la tupla es {tuplaColores[1]}')

tuplaNum = (1, 5, 6, 9, 7, 3, 5, 8, 4, 6, 2)
num = int(input("Ingresa un numero para ver si esta en la tupla: "))

elem = tuplaNum.count(num)
if elem == 0:
    print(f'El elemento {num} no se encuentra en la tupla')
else:
    print(f'El elemento {num} se encuentra en la tupla')


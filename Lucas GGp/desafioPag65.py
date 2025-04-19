"""Dada la siguiente lista:
amigos = ['ana', 'Monica', 'José', 'Camila', 'Raquel', 'Matías']
1 - Devuelve la posicion (el index, un numero) del amigo Matias
2 - Devuelve la misma lista pero añadiendo los amigos de la infancia 'Ivana' y 'Andres' como otra lista
3 - Agrega un nuevo amigp 'Maria' y devuelve el nro de amigos
4 - Elimina el ultimo elemento amigo y devuelve el nombre del amigo eliminado
5 - Devuelve un arreglo ordenado alfabeticamente"""

amigos = ['ana', 'Monica', 'José', 'Camila', 'Raquel', 'Matias']

index = amigos.index('Matias')
print(f"Matias se encuentra en la posicion {index}")

print('Concatenando dos listas')
amigos2 = ['Ivana', 'Andres']
amigosConcat = amigos + amigos2

print(amigosConcat)

print('Agregando un amigo Maria')
amigosConcat.append('Maria')
print(amigosConcat)

ultimoElem = amigosConcat[(len(amigosConcat))-1]
amigosConcat.pop()
print(f"Amigo eliminado {ultimoElem}")
print(amigosConcat)

amigosConcat.sort()
print('Elementos ordenados')
print(amigosConcat)

""" Escribe un programa que pida al usuario su año de nacimiento,
calcule su edad y genere un mensaje de saludo personalizado
que incluya su nombre y la edad calculada. """

añoNacimiento = int(input("Ingrese el año de nacimiento: "))
nombre = input("Ingresa tu nombre")

edad = 2025 - añoNacimiento 

print(f"Hola!{nombre} tu naciste en el año {añoNacimiento} y tu edad es de: {edad}")



# tenistas = []
# for jug in range(8):
#     jugador = input(f"Jugador {jug+1}")
#     tenistas.append(jugador)

tenistas = [
    "Roger Federer",
    "Rafael Nadal",
    "Novak Djokovic",
    "Serena Williams",
    "Steffi Graf",
    "Pete Sampras",
    "Andre Agassi",
    "Martina Navratilova"
]

ronda = 1
while len(tenistas) != 1:

    print(f"Ronda {ronda}")
    ganadores = []
    for jug in range(0, len(tenistas), 2):
        res = input(f"a: {tenistas[jug]} - b: {tenistas[jug+1]}: ")
        if res == "a":
            ganadores.append(tenistas[jug])
        else:
            ganadores.append(tenistas[jug+1])
    tenistas = ganadores
    ronda += 1

print(f"\nEl ganador es {tenistas[0]}")

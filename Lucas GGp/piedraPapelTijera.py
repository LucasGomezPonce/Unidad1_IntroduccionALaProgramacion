def resultadoDelVs(a, b):
    ganador = a
    if a == "piedra" and b == "tijera" or a == "papel" and b == "piedra" or a == "tijera" and b == "papel":
        pass
    else:
        ganador = b
    return ganador


contadorA = 0
contadorB = 0


while True:
    jugador = ["A", "B"]
    jugadas = []

    for j in jugador:
        print(f"""
Jugador {j}
Ingresa tu jugada: Piedra, Papel, Tijera: 
""")
        jugada = input(f"Ingrese su Jugada Jugador {j}: ")
        jugadas.append(jugada)

    if jugadas[0] == jugadas[1]:
        print("Empate")
    else:
        resGanador = resultadoDelVs(jugadas[0], jugadas[1])
        if resGanador == jugadas[0]:
            contadorA += 1

        else:
            contadorB += 1
        print(f"\n.:A:{contadorA} vs B:{contadorB}:.")

    if contadorA == 3 or contadorB == 3:
        if contadorA == 3:
            print("Ha ganado el jugador A")
        else:
            print("Ha ganado el jugador B")
        break

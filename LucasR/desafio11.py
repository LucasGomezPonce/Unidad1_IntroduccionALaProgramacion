import random

def janken():
    options = ['piedra', 'papel', 'tijera']
    victoty_player_a = 0
    victoty_player_b = 0

    while victoty_player_a <= 3 or victoty_player_b <= 3:
        player = input("Elige piedra, papel o tijera: ").lower()
        
        if player not in options:
            print("Opción no válida. Intentá de nuevo.")
            continue
        
        playerB = input("Elige piedra, papel o tijera: ").lower()

        if playerB not in options:
            print("Opción no válida. Intentá de nuevo.")
            continue
        
        print(f"La player eligió: {player}")
        print(f"La playerB eligió: {playerB}")

        if player == playerB:
            print("¡Empate!")
        elif (player == 'piedra' and playerB == 'tijera') or \
            (player == 'papel' and playerB == 'piedra') or \
            (player == 'tijera' and playerB == 'papel'):
            print("¡Ganaste esta ronda!")
            victoty_player_a += 1
        else:
            print("La playerB gana esta ronda.")
            victoty_player_b += 1

        print(f"Puntaje: jugador {victoty_player_a} - playerB {victoty_player_b}\n")

    if victoty_player_a == 3:
        print("¡Ganaste el juego!")
    else:
        print("La playerB ganó el juego.")
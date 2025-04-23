def RolandGarros ():
    tennisPlayers = []

    for name in range(8):
        player = input('Ingrese el nombre del tenista: ')
        tennisPlayers.append(player)

    
    round = 1
    while len(tennisPlayers) != 1:
        winners = []
        print(f"Ronda {round}")
        for jug in range(0, len(tennisPlayers), 2):
            res = input(f"a: {tennisPlayers[jug]} - b: {tennisPlayers[jug+1]}: ")
            if res == "a":
                winners.append(tennisPlayers[jug])
            else:
                winners.append(tennisPlayers[jug+1])
        tennisPlayers = winners

        if len(winners) == 2:
            print(f'La gran final: {winners[0]} vs {winners[1]}')
        
        if len(winners) == 1:
            print('🎊 Final del gran torneo Roland Garros 🎊')
            print(f'El ganador es {winners[0]} 🏆')
        else:
            print(winners)
        round += 1

    

RolandGarros()
import random
# Lista de Opciones
opciones = ["Piedra", "Papel", "Tijeras"]

# Computador Selecciona opción
def computador(opciones):
    npc = random.choice(opciones)
    return npc

# Jugabilidad
def cachipun(player, npc):
    print(f'\nEl computador eligió {npc}...\n')
    if (player == npc):
        print('Empatados....\n')
        print('Fin del juego')
    else:
        if (player=='Piedra' and npc=='Tijeras') or ( player=='Papel' and npc=='Piedra') or ( player=='Tijeras' and npc=='Papel'):
            print('Has Ganado! Felicitaciones :D \n')
            print('Fin del juego')
        else:
            print('Ding....ding....ding.... El computador Ganó')
            print('Fin del juego')


# Entrada del Jugador
def jugar():
    npc = computador(opciones)
    player = (input('¿Piedra, Papel o Tijeras?\n'))
    if player.capitalize() not in(opciones):
        print('Debes usar las Jugadas Listadas')
        return jugar()
    else:
        return cachipun(player, npc)

# iniciar el Juego
jugar()

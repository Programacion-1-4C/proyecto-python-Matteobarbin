import random
import sys

jugadorest = "perez,diaz,vilagra,valoyes,herrera,aguerre,benavidez,catalan,martino,malatini,franco,garro,esquivel,godoy,ortegoza,bufarini,suarez,girotti,santos,romero,fertoli"
jugadorest = jugadorest.split(",")
final_jugadorest = []
for x in jugadorest:
    jugadorest = x.strip()
    final_jugadorest.append(jugadorest)

puntos = 0

def adivinaeljugadort():
    global puntos
    print("juego de futbol -adivina el nombre del jugador")
    print("lista de jugadorest ...tenes que adivinar el nombre de un jugadort ramdom")
    print(final_jugadorest)
    random_final_jugadorest = random.choice(final_jugadorest)
    print(random_final_jugadorest[0] + "-"*(len(random_final_jugadorest)-2) + random_final_jugadorest[-1])

    user_input = str(input("adivina el nombre del jugadort : "))
    if user_input == random_final_jugadorest :
        puntos +=1
        print("puntos:", puntos)
        adivinaeljugadort()
    else:
        print("")
        print("")

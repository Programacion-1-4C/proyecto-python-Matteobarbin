import random
import sys


def adivina_el_jugadort(puntos, final_jugadorest):
    print("juego de futbol -adivina el nombre del jugador")
    print("lista de jugadorest ...tenes que adivinar el nombre de un jugadort ramdom")
    print(final_jugadorest)
    random_final_jugadorest = random.choice(final_jugadorest)
    print(random_final_jugadorest[0] + "-" * (len(random_final_jugadorest) - 2) + random_final_jugadorest[-1])

    user_input = input("adivina el nombre del jugadort : ")
    if user_input == random_final_jugadorest:
        puntos += 1
        print("puntos:", puntos)
        adivina_el_jugadort(puntos, final_jugadorest)
    else:
        print("uyyy!respesta incorrecta,la respuesta correcta es:{}".format(random_final_jugadorest))
        print("su cantidad de puntos es:{}".format(str(puntos)))
        jugar_de_vuelta = input("te gustaria volver a jugar").lower()
        if jugar_de_vuelta in ["si", "s"]:
            puntos = 0
            adivina_el_jugadort(puntos, final_jugadorest)
        else:
            sys.exit("nos vemos !!")


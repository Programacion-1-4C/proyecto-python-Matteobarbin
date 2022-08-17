import random
import sys
from funcionmenu import adivina_el_jugadort

jugadorest = "perez,diaz,villagra,valoyes,herrera,aguerre,benavidez,catalan,martino,malatini,franco,garro,esquivel,godoy,ortegoza,bufarini,suarez,girotti,santos,romero,fertoli"
jugadorest = jugadorest.split(",")
final_jugadorest = []
for x in jugadorest:
    jugadorest = x.strip()
    final_jugadorest.append(jugadorest)
puntos = 0
while True:
    print("1.ingrese un nuevo jugador")
    print("2.vamo a jugar")
    operacion = int(input(""))
    if operacion == 1:
        nuevo_jugadorest = str(input("ingrese un nuevo jugador"))
        final_jugadorest.append(nuevo_jugadorest)

    if operacion == 2:
        adivina_el_jugadort(puntos, final_jugadorest)


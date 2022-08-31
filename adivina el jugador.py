from funcionmenu import adivina_el_jugadort
#importamoa la funcion adivina_el_jugadort
contraseña =123
#contraseña es 123
contra=int(input("ingrese la contraseña>>>"))
if contra==contraseña:
    print("contraseña correcta")
    #aca armamos la contraseña si es correcta seguimos con el programa

    jugadorest = "perez,diaz,villagra,valoyes,herrera,aguerre,benavidez,catalan,martino,malatini,franco,garro,esquivel,godoy,ortegoza,bufarini,suarez,girotti,santos,romero,fertoli "
    #lista de jugadores de talleres
    jugadorest = jugadorest.split(",")
    #esto lo hice para separar cada jugador con ","
    final_jugadorest = []
    #lista final con los jugadores separados con","

    for x in jugadorest:
        jugadorest = x.strip()
        final_jugadorest.append(jugadorest)
    puntos = 0


    while True:
        print("1.ingrese un nuevo fichaje")
        print("2.vamo a jugar")
        operacion = int(input(""))
        #menu

        if operacion == 1:
            nuevo_jugadorest = str(input("ingrese un nuevo fichaje"))

            if nuevo_jugadorest not in final_jugadorest:
                final_jugadorest.append(nuevo_jugadorest)
                #si el jugador no esta en a lista lo agregamos
            else:
                print("el jugador ya esta en la lista")
                #si si esta no lo agregamos

        if operacion == 2:
            adivina_el_jugadort(puntos, final_jugadorest)
            #usamos la funcion para adivinar jugadores
else :
  print("contraseña incorrecta")
# si contraseña es incorrecta vole a intentar ( es 123)

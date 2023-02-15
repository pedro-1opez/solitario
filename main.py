import funciones

def main():

    #Genera el mazo
    mazo = funciones.generar_mazo()

    #Genera la mano del jugador
    jugador = funciones.obten_mano(mazo)
    jugador = sorted(jugador)

    #Genera la mano del CPU
    cpu = funciones.obten_mano(mazo)
    cpu = sorted(cpu)        

    #Contamos los puntos
    j = funciones.contar_puntos(jugador)
    c = funciones.contar_puntos(cpu)

    #Determinamos quien gano
    if j > c:
        print("Gano Jugador")    
    else:
        if j < c:
            print("Gano CPU")
        else:
            print("Empate")

if __name__ == "__main__":
    main()    
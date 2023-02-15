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

if __name__ == "__main__":
    main()    
from random import choice

def generar_mazo():
    numeros = [f"{x}" for x in range(2,11)] 
    letras = ["J","Q","K","A"] 
    simbolos = ["♥","♦","♣","♠"] 

    numeros.extend(letras)
    mazo = []

    for s in simbolos:
        for n in numeros:
            mazo.append([n,s])

    jokers = ["?","?"]
    mazo.extend(jokers)

    return mazo

def obten_carta(mazo):
    carta = choice(mazo)
    mazo.remove(carta)

    return carta

def obten_mano(baraja:list) -> list:    
    
    mano = []

    for i in range(0,5):
        carta = obten_carta(baraja)
        mano.append(carta)
        
    return mano

def contar_puntos(jugador:list) -> int:
        diccionario = {}    

        for carta in jugador:
            if carta[0] in diccionario:
                diccionario[carta[0]] += 1
            else:
                diccionario[carta[0]] = 1
    
        puntos = 0

        for k,v in diccionario.items():
            if v == 2:
                if k in ['J','Q','K']:
                    puntos += 11
                elif k == 'A':
                    puntos += 12
                elif k.isdigit():
                    puntos += int(k)

            if v == 3:
                if k in ['J','Q','K']:
                    puntos += 110
                if k == 'A':
                    puntos += 120
                else:
                    puntos += (int(k)*10)

        return puntos

def crea_conteo(mano: list) -> dict:
    
    d = {'A':2,
         '3':2,
         '?':1}

    for carta in mano:
        if carta[0] in d:
            d[carta[0]] += 1
        else:
            d[carta[0]] = 1
            
    return d
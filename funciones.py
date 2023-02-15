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
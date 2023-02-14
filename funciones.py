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
def calcola_quadrati():

    numeri = [0, 1, 2, 3, 4, 5]
    
    # map applica la funzione a ogni elemento della lista
    quadrati = list(map(lambda x: x**2, numeri))
    
    return quadrati

risultato = calcola_quadrati()
print(risultato)
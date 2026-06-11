# Chiedi all'utente di inserire un numero. 
# Il programma dovrebbe quindi fare un conto alla rovescia a partire da quel numero fino a zero,
# stampando ogni numero e chiederti se vuoi ripetere o no.

while True: #ripetizione in loop nel caso si vuole ripetere
    numero = int(input("Inserisci un numero: "))

    while numero >= 0:
        print(numero)
        numero -= 1 #decremento il contatore

    scelta = input("Vuoi ripetere? (si/no): ")

    if scelta.lower() != "si":
        print("Programma terminato.")
        break
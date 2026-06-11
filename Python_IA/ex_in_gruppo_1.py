# Inizializziamo la variabile per accumulare la somma
somma = 0

# Chiediamo il primo numero all'utente
numero = int(input("Inserisci un numero intero (0 per terminare): "))

# Finché il numero inserito è diverso da 0, il ciclo continua
while numero != 0:
    somma += numero  # Aggiungiamo il numero alla somma totale
    # Chiediamo un nuovo numero per evitare un ciclo infinito
    numero = int(input("Inserisci un altro numero (0 per terminare): "))

# Quando il ciclo finisce, stampiamo il risultato
print(f"\nIl ciclo è terminato. La somma totale è: {somma}")
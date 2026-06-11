# Scrivi un programma Python che segua esattamente questi passaggi:

# Inizializzazione: Crea una lista chiamata prodotti che contenga tre capi d'abbigliamento (es: "Maglietta", "Pantaloni", "Felpa").

# Espansione: Chiedi all'utente di digitare il nome di un nuovo prodotto da aggiungere al catalogo e aggiungilo alla lista.

# Creazione Inventario: Crea un dizionario chiamato magazzino. Le chiavi devono essere i prodotti presenti nella lista e i valori devono essere tutti impostati a una quantità fissa iniziale (es: 10 per tutti).

# Selezione: Mostra all'utente la lista dei prodotti. Chiedi all'utente di inserire l'indice (il numero di posizione) del prodotto che desidera acquistare.

# Aggiornamento: Chiedi all'utente quanti pezzi di quel prodotto vuole prelevare. Sottrai quel numero dalla quantità presente nel dizionario magazzino.

# Riepilogo: Stampa a video il dizionario finale per mostrare le quantità aggiornate.

# Inizializzazione traccia
prodotti = ["maglietta", "pantaloni", "felpa"]

# Espansione traccia
nuovo_prodotto = input("Inserisci un nuovo prodotto: ")
prodotti.append(nuovo_prodotto)

print(prodotti)

# Creazione dizionario magazzino
magazzino = {
    prodotti[0]: 10,
    prodotti[1]: 10,
    prodotti[2]: 10,
    prodotti[3]: 10
}

print (magazzino)

# Selezione traccia
indice = int(input("Inserisci l'indice del prodotto da acquistare (gli indici partono dalla posizione 0): "))
prodotto_scelto = prodotti[indice]

# Aggiornamento traccia
quantita = int(input("Quanti pezzi vuoi acquistare? "))
magazzino[prodotto_scelto] = magazzino[prodotto_scelto] - quantita

# Riepilogo traccia
print("Magazzino aggiornato:", magazzino)
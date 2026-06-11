# Dati Paralleli: * Crea una lista nomi con due capi: "Giacca", "Scarpe".

# Crea una lista codici con i rispettivi ID: "SKU-01", "SKU-02".

# Espansione Manuale: * Chiedi all'utente di inserire un nuovo nome e un nuovo codice.

# Aggiungili alle rispettive liste (fai in modo che il codice sia salvato tutto in maiuscolo).

# Il Listino Prezzi: * Crea un dizionario prezzi. Le chiavi devono essere i codici della lista codici e i valori devono essere i prezzi (es: 120.0, 80.0, 50.0).

# Il Registro Disponibilità: * Crea un dizionario disponibile (Booleano). Usa i codici come chiavi e imposta tutto a True.

# L'Operazione di Vendita:

# Mostra all'utente le liste. Chiedi di inserire l'indice del prodotto acquistato.

# Il Ponte: Recupera il codice corrispondente a quell'indice dalla lista codici.

# L'Aggiornamento: * Applica uno sconto del 10% al prezzo di quel codice nel dizionario prezzi.

# Cambia lo stato di quel codice nel dizionario disponibile in False.


# Scrivi un programma Python che segua esattamente questi passaggi:

# Inizializzazione: Crea una lista chiamata prodotti che contenga tre capi d'abbigliamento (es: "Maglietta", "Pantaloni", "Felpa").

# Espansione: Chiedi all'utente di digitare il nome di un nuovo prodotto da aggiungere al catalogo e aggiungilo alla lista.

# Creazione Inventario: Crea un dizionario chiamato magazzino. Le chiavi devono essere i prodotti presenti nella lista e i valori devono essere tutti impostati a una quantità fissa iniziale (es: 10 per tutti).

# Selezione: Mostra all'utente la lista dei prodotti. Chiedi all'utente di inserire l'indice (il numero di posizione) del prodotto che desidera acquistare.

# Aggiornamento: Chiedi all'utente quanti pezzi di quel prodotto vuole prelevare. Sottrai quel numero dalla quantità presente nel dizionario magazzino.

# Riepilogo: Stampa a video il dizionario finale per mostrare le quantità aggiornate.

# 3° esercizio
# Definizione liste originali
Nomi = ["Giacca", "Scarpe"]
Codici = ["SKU-01", "SKU-02"]

# Inserimento nuovo prodotto
print('Questi sono i capi in collezione', Nomi)
Nomi.append(str(input('Inseriscine uno nuovo: ')))
print('Questi sono i codici dei primi due prodotti', Codici)
Codici.append(str(input('inseriscine uno per il nuovo capo: ')).upper())

# Definizione del magazzino
Listino = {str(Nomi[0]): 120, str(Nomi[1]): 100, str(Nomi[2]): 50}
Disponibilita = {str(Codici[0]): True, str(Codici[1]): True, str(Codici[2]): True}

# Fase di acquisto
print('Sono presenti i seguenti prodotti: ', Nomi)
cod = int(input('Seleziona il prodotto che ti interessa inserendone il codice posizione: '))
print('Il prodotto selezionato corrisponde al codice ', Codici[cod])

# sconto del 10% ed aggiornamento disponibilità
c = Listino[str(Nomi[cod])] 
c = (9*c)/10
Listino[str(Nomi[cod])] = c
Disponibilita[str(Codici[cod])] = False

# Riepilogo finale
print('Il prodotto venduto è:', Nomi[cod], 'al prezzo scontato di', Listino[str(Nomi[cod])])
print(Listino, Disponibilita)

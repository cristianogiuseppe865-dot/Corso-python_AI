# Esercizio 8
# Scrivi un programma in Python che simuli un  gestore di pacchi  utilizzando più classi; 

# sono ammessi solo classi, oggetti, funzioni, metodi e al massimo liste o dizionari.

# Il sistema deve includere una classe Pacco con: codice (stringa), peso (numero) 

# e stato (es. "in magazzino", "in consegna", "consegnato"), con un metodo per mostrare le info e un metodo per cambiare stato. 

# Deve esserci una classe Magazzino che contiene una lista (o dizionario) 

# di pacchi e permette di aggiungere un pacco, cercarlo per codice, e mostrare tutti i pacchi in un certo stato. 

# Deve esserci infine una classe GestorePacchi che usa il magazzino per mettere un pacco “in consegna”,

# segnare un pacco come “consegnato” e calcolare il peso totale dei pacchi ancora non consegnati.

# Nel programma principale crea almeno 5 pacchi, inseriscili nel magazzino, 

# cambia lo stato di alcuni pacchi (almeno una consegna avviata e una consegna completata)

#  e stampa: elenco pacchi “in magazzino”, elenco pacchi “in consegna” e il peso totale dei pacchi non ancora consegnati.




#main


import classe_gestione_pacchi, classe_magazzino, classe_pacco


mio_magazzino = classe_magazzino.Magazzino()
gestore = classe_gestione_pacchi.GestorePacchi(mio_magazzino)

# Creazione automatica di 5 pacchi (oggetti) per testare subito il programma
mio_magazzino.aggiungi_pacco(classe_pacco.Pacco("A1", 2.0))
mio_magazzino.aggiungi_pacco(classe_pacco.Pacco("B2", 5.5))
mio_magazzino.aggiungi_pacco(classe_pacco.Pacco("C3", 1.2))
mio_magazzino.aggiungi_pacco(classe_pacco.Pacco("D4", 3.0))
mio_magazzino.aggiungi_pacco(classe_pacco.Pacco("E5", 0.5))

print("Magazzino inizializzato con 5 pacchi (Stato: in magazzino)")

# Ciclo infinito per permettere all'utente di fare più operazioni
while True:
    print("\n--- MENU GESTIONE PACCHI ---")
    print("1) Metti in consegna")
    print("2) Segna come consegnato")
    print("3) Cerca pacco per codice")
    print("4) Mostra pacchi per stato")
    print("5) Calcola peso totale non consegnati")
    print("6) Esci")
    
    scelta = input("Cosa vuoi fare? ")

    if scelta == "1":
        gestore.metti_in_consegna()
    elif scelta == "2":
        gestore.segna_consegnato()
    elif scelta == "3":
        mio_magazzino.cerca_pacco()
    elif scelta == "4":
        mio_magazzino.pacco_instato()
    elif scelta == "5":
        peso = gestore.calcola_peso_non_consegnati()
        print(f"Peso totale pacchi (in magazzino + in consegna): {peso} kg")
    elif scelta == "6":
        print("Chiusura programma...")
        break
    else:
        print("Opzione non valida.")
# ## Esercizio: Sfida all'Ultimo Dado (Player vs AI)

# ---

# ### **Descrizione**
# In questo gioco, un giocatore umano sfida l'Intelligenza Artificiale in un duello di **5 turni**. In ogni turno, entrambi lanciano un dado magico. Il punteggio non dipende solo dal numero uscito, ma da alcune **regole speciali** che dovrai programmare utilizzando le funzioni per gestire la logica di gioco.

# ---

# ### **Regole del Gioco (La Logica)**
# Il punteggio per ogni singolo lancio viene calcolato seguendo questi criteri:

# * **Se esce 1:** È un "Fumble" (fallimento critico). Il giocatore riceve **-2 punti**.
# * **Se esce 6:** È un "Colpo Critico". Il giocatore riceve **10 punti**.
# * **Se esce qualsiasi altro numero:** Il punteggio guadagnato è uguale al valore nominale della **faccia del dado**.

# ---

# ### **Requisiti del Codice**
# Il programma deve essere strutturato obbligatoriamente con le seguenti funzioni:

# 1.  **`lancia_dado()`**
#     * Non riceve parametri.
#     * Restituisce un numero casuale tra **1** e **6** (inclusi).
# 2.  **`calcola_punti(faccia)`**
#     * Riceve come parametro il valore del dado appena lanciato.
#     * Applica le regole speciali e **restituisce** il punteggio ottenuto in quel turno.
# 3.  **`mostra_situazione(punti_utente, punti_ai)`**
#     * Riceve i due punteggi totali.
#     * Stampa a video il riepilogo e indica chi è in vantaggio o se la sfida è in pareggio.
# 4.  **`partita()`**
#     * È la funzione principale (Main).
#     * Deve contenere un ciclo per gestire i **5 turni**.
#     * Coordina le chiamate alle altre funzioni, aggiorna i punteggi e dichiara il vincitore finale.

# ---

# ### **Scheletro del Progetto**

# ```python
# import random

# def lancia_dado():
#     """Genera e restituisce un numero casuale tra 1 e 6."""
#     pass

# def calcola_punti(faccia):
#     """Riceve la faccia e restituisce il punteggio calcolato."""
#     pass

# def mostra_situazione(punti_utente, punti_ai):
#     """Stampa i punteggi attuali e chi sta vincendo."""
#     pass

# def partita():
#     """Funzione principale: gestisce i 5 turni e i punteggi totali."""
#     # Inizializza i punteggi
#     # Ciclo for per i turni
#     # Logica di vittoria finale
#     pass

# if __name__ == "__main__":
#     partita()

import random


def lancia_dado():
    
    return random.randint(1, 6)


def calcola_punti(faccia):
    
    if faccia == 1:
        return -2
    elif faccia == 6:
        return 10
    else:
        return faccia


def mostra_situazione(punti_utente, punti_ai):
    
    print("\n--- SITUAZIONE ATTUALE ---")
    print("Utente:", punti_utente)
    print("AI:", punti_ai)

    if punti_utente > punti_ai:
        print("Sei in vantaggio!")
    elif punti_utente < punti_ai:
        print("L'AI è in vantaggio!")
    else:
        print("Siete in pareggio!")


def partita():

    punti_utente = 0
    punti_ai = 0

    print("Inizia la sfida all'ultimo dado!")

    for turno in range(1, 6):
        print("\n--- Turno", turno, "---")

        dado_utente = lancia_dado()
        punti_utente += calcola_punti(dado_utente)
        print("Tu hai fatto:", dado_utente)

        dado_ai = lancia_dado()
        punti_ai += calcola_punti(dado_ai)
        print("AI ha fatto:", dado_ai)

        mostra_situazione(punti_utente, punti_ai)

    print("\n RISULTATO FINALE")

    if punti_utente > punti_ai:
        print("Hai vinto la partita!")
    elif punti_utente < punti_ai:
        print("Ha vinto l'AI")
    else:
        print("Pareggio!")


partita()
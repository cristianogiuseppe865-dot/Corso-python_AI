# --- SMART VENDOR 2000 ---
## Sfide Extra

# Per chi finisce in anticipo o vuole rendere il progetto davvero professionale:

# *   ** Livello 1: Gestione Magazzino**
#     Aggiungi una terza lista chiamata `quantita` (es. ogni prodotto parte da 5 pezzi). 
# Ogni volta che un prodotto viene acquistato, 
# la quantità scende. Se arriva a zero, 
# il distributore deve mostrare la scritta "ESAURITO" e impedire l'acquisto.
# *   ** Livello 2: Codice Sconto "Happy Hour"**
#     All'inizio del programma, chiedi all'utente se ha un codice sconto.
# Se inserisce `ESTATE2026`, applica uno sconto del **20%** 
# a tutti i prezzi del listino prima di iniziare il ciclo di vendita.
# *   ** Livello 3: Modalità Manutentore (Secret Menu)**
#     Se l'utente inserisce un codice segreto (es. `9999`) nel menu principale, '
#     'accedi a un menu nascosto che mostra l'**incasso totale** del distributore 
# (quanti soldi ha effettivamente guadagnato la macchina fino a quel momento).
# *   ** Livello 4: Validazione Tagli di Moneta**
#     Il distributore non accetta monete strane! Permetti l'inserimento solo di tagli validi:'
#     ' `0.10, 0.20, 0.50, 1.00, 2.00`. Se l'utente inserisce `0.35`, rifiuta la moneta.
def mostra_menu():
    #semplice stampa
    print("\n--- MENU ---")
    print("1. Inserisci le monete")
    print("2. Seleziona il prodotto")
    print("3. Visualizza credito")
    print("4. Esci e resto")

#def gestione_quantita()

def inserisci_monete(credito_attuale):
    #operazione iniziale per le monete
    #lista monete valide
    monete_valide=[0.10, 0.20, 0.50, 1.00, 2.00]
    importo = float(input("Inserisci un importo. Si accetano monete queste monete 0.10, 0.20, 0.50, 1.00, 2.00 "))
    #se l'importo messo dall'utente è una moneta valida
    if importo in monete_valide:
        print("Moneta inserite")
        print("Il credito è stato aggiornato")
        return credito_attuale + importo
    else:
        print ("Moneta non valida")
        return credito_attuale
def mostra_prodotti(prodotti, prezzi,quantita):
    print("\n--- LISTINO ---")
    # ciclo per ogni i nel range lunghezza lista prodotti 
    for i in range(len(prodotti)):
        
        print(f"[{i}] {prodotti[i]} - {prezzi[i]:.2f}€ quantita:{quantita[i]}")
# Nomi diversi, stesso valore: sel e scelta contengono lo stesso dato (es. il numero 1), perchè sono posizionati nello "slot 1 " 
# # ma hanno nomi diversi perché vivono in "stanze" diverse del programma.
def gestisci_acquisto(scelta, prodotti, prezzi, credito_attuale,quantita):
    indice = int(scelta)
    # indice deve essere compreso tra 0 e la lunghezza della lista
    if 0 <= indice < len(prodotti):
        if quantita[indice]<=0:
            print("prodotto esaurito ")
        #prezzo per i vari indici
        prezzo_scelto = prezzi[indice]
        
        if credito_attuale >= prezzo_scelto:
            print(f"Erogazione: {prodotti[indice]}")
            quantita[indice] -=1
            #quantita_aggiornata = quantita -1
            #ritorniamo l'aggiornamento del credito con la sottrazione
            return credito_attuale - prezzo_scelto ,prezzo_scelto 
           
        else:
            manca = prezzo_scelto - credito_attuale
            print(f"Mancano {manca:.2f} euro")
    else:
        print("Selezione errata")

    return credito_attuale

def main():
    prodotti = ["Coca-Cola", "Acqua", "Patatine", "Cioccolato"]
    prezzi = [1.50, 0.80, 1.20, 1.00]
    quantita=[5,8,5,7]
    credito = 0.0
    incasso= 0.0
    in_esecuzione = True
   
    print("--- Benvenuti in Smart Vendor 2000 ---")
    codice = input("Hai un codice sconto? Se si inseriscilo. ")
    if codice == "ESTATE2026":
        for i in range(len(prezzi)):
            prezzi[i] *=0.80
    while in_esecuzione:
        mostra_menu()
        scelta_utente = input("\nCosa desideri fare? ")

        if scelta_utente == "1":
            #  Dobbiamo assegnare il ritorno della funzione alla variabile credito per l' aggiornamento
            credito = inserisci_monete(credito)
            
        elif scelta_utente == "2":
            mostra_prodotti(prodotti, prezzi,quantita)
            #scelta del'utente per la gestione dell'acquisto
            sel = input("Quale indice? ")
            #gestione della doppia variabile perchè in entrambe ti servono i return di gestione acquisto
            #viene preso direttamente sel in questo main perchè scelta nella funzione è passato come parametro
            #----MOLTO IMPORTANTE NON INVERTIRE CREDITO E GUADAGNO PERCHE LA MACCHINA 
            # NON SA COSA SIANO EFFETTIVAMENTE MA GESTISCE LA SITUAZIONE IN BASE AL PUNTO IN CUI SI TROVA
            #QUESTA E' UNA  GESTIONE DOPPIA DEI DUE RETURN DELLA FUNZIONE 
            #CREDITO RIGUARDA L'UTENTE
            #GUADAGNO RIGUARDA LATO ADMIN INFATTI RIGUARDA SOLO IL PREZZO SCELTO CHE HA PAGATO L UTENTE
            credito,guadagno= gestisci_acquisto(sel, prodotti, prezzi, credito,quantita)

            incasso += guadagno
            
        elif scelta_utente == "3":
            
            print(f"Credito attuale: {credito:.2f}€")
            
        elif scelta_utente == "4":
            print(f"Resto erogato: {credito:.2f}€")
            print("Arrivederci!")
            in_esecuzione = False 
        
        elif scelta_utente =="9999":
            print("Modalita admin ")
            print(f"Incasso {incasso:.2f} euro")
        else:
            print("Comando non valido.")

# Avvio del programma
if __name__ == "__main__":
    main()
# Definizione della classe Magazzino che contiene la lista dei pacchi
class Magazzino:
    def __init__(self):
        self.lista_pacchi = [] # Lista vuota che conterrà gli oggetti di tipo Pacco

    # Metodo per aggiungere un oggetto Pacco alla lista
    def aggiungi_pacco(self, pacco):
        self.lista_pacchi.append(pacco)
            
    # Metodo per cercare un pacco digitando il codice
    def cerca_pacco(self):
        codice_ricercato = input("Inserisci il codice da cercare: ")
        trovato = False
        
        # ERRORE PRECEDENTE: for Pacco.codice in self.lista_pacchi:
        # SPIEGAZIONE: Non puoi usare 'NomeClasse.attributo' come variabile di ciclo. 
        # Devi usare una variabile temporanea (come 'p') che rappresenta il pacco corrente nella lista.
        for p in self.lista_pacchi:
            if p.codice == codice_ricercato:
                print("Pacco trovato!")
                p.info() # Richiama il metodo info dell'oggetto trovato
                trovato = True
                break
        if not trovato:
            print("Pacco non presente")

    # Metodo per mostrare tutti i pacchi che hanno un determinato stato
    def pacco_instato(self):
        stato_cercato = input("Quale stato vuoi cercare? (in magazzino/in consegna/consegnato): ")
        print(f"\n--- Pacchi in stato: {stato_cercato} ---")
        for p in self.lista_pacchi:
            # ERRORE PRECEDENTE: if s == stato_cercato:
            # SPIEGAZIONE: 's' era l'intero oggetto Pacco, non potevi confrontarlo direttamente con una stringa.
            # Bisogna accedere all'attributo .stato dell'oggetto (p.stato).
            if p.stato == stato_cercato:
                p.info()
# Definizione della classe Pacco
class Pacco:
    # Il costruttore inizializza il pacco. Lo stato ha un valore di default "in magazzino"
    def __init__(self, codice, peso, stato="in magazzino"):
        self.codice = codice
        self.peso = peso
        self.stato = stato

    # Metodo per stampare le informazioni del pacco
    def info(self):
        # ERRORE PRECEDENTE: print(f"Il pacco:{self.nome}...") 
        # SPIEGAZIONE: La variabile 'self.nome' non esisteva, avevi definito 'self.codice' nel costruttore.
        print(f"Il pacco: {self.codice} | Peso: {self.peso}kg | Stato: {self.stato}")

    # Metodo per modificare lo stato tramite input
    def modifica(self):
        stato_pacco = input("Modifica lo stato del pacco (in magazzino/in consegna/consegnato): ")
        
        # ERRORE PRECEDENTE: if stato_pacco != "consegnato" or "in consegna" or "in magazzino":
        # SPIEGAZIONE: In Python, questa sintassi è sbagliata perché valuta le stringhe dopo l'or come sempre "vere".
        # Si usa 'not in' seguito da una lista [] per confrontare più valori correttamente.
        if stato_pacco not in ["consegnato", "in consegna", "in magazzino"]:
            print("Errore operazione") 
        else: 
            print("Operazione andata a buon fine")
            self.stato = stato_pacco
            print("Nuovo stato:", self.stato)
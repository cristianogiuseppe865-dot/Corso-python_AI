# Classe per gestire le operazioni di consegna e calcoli logistici
class GestorePacchi:
    def __init__(self, magazzino):
        self.magazzino = magazzino # Riceve l'oggetto magazzino per operare sulla sua lista

    # Cambia lo stato di un pacco cercandolo per codice
    def metti_in_consegna(self):
        codice = input("Inserisci il codice del pacco da mettere in consegna: ")
        for p in self.magazzino.lista_pacchi:
            if p.codice == codice:
                p.stato = "in consegna"
                print(f"Pacco {codice} ora in consegna.")
                return
        print("Pacco non trovato.")

    # Segna un pacco come consegnato
    def segna_consegnato(self):
        codice = input("Inserisci il codice del pacco consegnato: ")
        for p in self.magazzino.lista_pacchi:
            if p.codice == codice:
                p.stato = "consegnato"
                print(f"Pacco {codice} consegnato con successo.")
                return
        print("Pacco non trovato.")

    # Calcola la somma dei pesi dei pacchi non ancora arrivati a destinazione
    def calcola_peso_non_consegnati(self):
        totale = 0
        for p in self.magazzino.lista_pacchi:
            if p.stato != "consegnato":
                totale += p.peso
        return totale
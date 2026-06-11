# classe persona con nome e portafoglio (privata) 
# e lista della spesa vuota
# lista di prodotti con prezzi che l'utente può comprare, 
# tutti i controlli di aggiornamento valori devono
# stare nelle properties della classe

class Persona:

    # costruttore
    def __init__(self, nome, portafoglio):

        self.nome = nome

        # variabile privata
        self._portafoglio = portafoglio

        # lista spesa vuota
        self.spesa = []

    # getter
    @property
    def portafoglio(self):

        # restituisce il valore del portafoglio
        return self._portafoglio

    # setter
    @portafoglio.setter
    def portafoglio(self, valore):

        # controlla se il saldo basta
        if self._portafoglio >= valore:

            # rimuove i soldi
            self._portafoglio -= valore

        else:
            print("saldo insufficiente")

    # acquisto prodotto
    def rimozione_soldi(self, prodotto, valore):

        # usa il setter
        self.portafoglio = valore

        # aggiunge il prodotto alla lista spesa
        if self._portafoglio >= 0:
            self.spesa.append(prodotto)


def main():

    persona = Persona("roberto", 5)

    prodotti = {
        "latte": 5,
        "pane": 4,
        "uova": 3
    }

    print(prodotti)

    persona.rimozione_soldi("latte", prodotti["latte"])

    persona.rimozione_soldi("pane", prodotti["pane"])

    persona.rimozione_soldi("uova", prodotti["uova"])

    print(persona.portafoglio)

    print(persona.spesa)


main()
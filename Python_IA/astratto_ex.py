from abc import ABC, abstractmethod


class Impiegato(ABC):
    def __init__(self, nome, cognome, stipendio_base):
        self.nome = nome
        self.cognome = cognome
        self.stipendio_base = stipendio_base

    @abstractmethod
    def calcola_stipendio(self):
        pass

    def __str__(self):
        return f"{self.nome} {self.cognome}"



class ImpiegatoFisso(Impiegato):
    def calcola_stipendio(self):
        # Riceve esattamente lo stipendio base
        return self.stipendio_base

class ImpiegatoAProvvigione(Impiegato):
    def __init__(self, nome, cognome, stipendio_base, vendite, percentuale):
        super().__init__(nome, cognome, stipendio_base)
        self.vendite = vendite
        self.percentuale = percentuale

    def calcola_stipendio(self):
        # Calcolo: Base + (Vendite * Percentuale)
        bonus = self.vendite * (self.percentuale / 100)
        return self.stipendio_base + bonus

def stampa_report_stipendi(lista_impiegati):
    # scorre ogni impiegato nella lista impiegati
    for impiegato in lista_impiegati:
        totale = impiegato.calcola_stipendio()
        print(f"Impiegato: {impiegato}  Totale da pagare: {totale:.2f}€")

peppe = ImpiegatoFisso("Peppe", "Rossi", 1500)
luca = ImpiegatoAProvvigione("Luca", "Rossi", 1200, vendite=5000, percentuale=10)

# Lista degli impiegati
personale = [peppe, luca]
stampa_report_stipendi(personale)
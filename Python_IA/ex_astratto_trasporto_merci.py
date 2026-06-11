# Esercizio: Sistema Astratto di Trasporto Merci


# Requisiti
# 1. Classe Astratta: VeicoloTrasporto
# Crea una classe astratta chiamata VeicoloTrasporto, che rappresenti un veicolo generico per il trasporto di merci.


        

# La classe deve contenere:

# Attributi comuni (protetti)
# _targa : stringa

# _peso_massimo : intero (capacità di carico in kg)

# _carico_attuale : intero (inizialmente 0)

# Metodi
# Un costruttore che inizializza i campi comuni.

# Un metodo concreto:

# carica(peso)

#  Aumenta il carico attuale se possibile, altrimenti segnala che il peso supera la capacità.

# Un metodo concreto:

# scarica()

#  Riporta il carico attuale a 0.

# Un metodo astratto:

# costo_manutenzione()

#  Ogni veicolo deve avere un costo di manutenzione calcolato secondo regole diverse.


# 2. Sottoclassi Concrete
# Crea almeno tre sottoclassi che estendono la classe astratta e implementano il metodo costo_manutenzione() secondo regole differenti:

# a) Camion
# Attributo extra: numero_assi

# Regola manutenzione (esempio):

# 100 € per asse + 1 € per kg di carico massimo

# b) Furgone
# Attributo extra: alimentazione (es. “diesel”, “elettrico”)

# Regola manutenzione:

# Se elettrico: 200 €

# Se diesel: 150 €

# c) Motocarro
# Attributo extra: anni_servizio

# Regola manutenzione:

# 50 € per ogni anno di servizio


# 3. Classe GestoreFlotta
# Crea una classe che gestisca un elenco di veicoli:

# Attributi
# veicoli: lista di oggetti derivati da VeicoloTrasporto.


# Metodi
# aggiungi_veicolo(veicolo)

# rimuovi_veicolo(targa)

# costo_totale_manutenzione():

#  Somma dei costi di manutenzione di tutti i veicoli (polimorfismo sugli oggetti astratti).

# stampa_veicoli():

#  Elenca targa, tipo e carico attuale.

from abc import ABC,abstractmethod

class VeicoloTrasporto(ABC):
    
    def __init__(self,_targa,_peso_massimo,_carico_attuale):
        self._targa= _targa
        self._peso_massimo=_peso_massimo
        self._carico_attuale=_carico_attuale
        _carico_attuale= 0
    
    def carica(self,peso):
        
        if peso < self._peso_massimo:
            return self._carico_attuale + peso
        else:
            print("Il peso supera il peso massimo")
    def scarica(self):
        self._carico_attuale = 0
        print("il peso è stato scaricato adesso il carico è 0") 
    @abstractmethod
    def costo_manutenzione(self):
        pass
    
class Camion(VeicoloTrasporto):
    def __init__(self,_targa,_peso_massimo,_carico_attuale,_numero_assi ):
        super().__init__(self,_targa,_peso_massimo,_carico_attuale)
        self._numero_assi=_numero_assi
        
    def costo_manutenzione(self,costo):
        costo = (self._numero_assi * 100) + (1*self._peso_massimo)
        return costo
camion = Camion("aaa",40,0,5)
print(Camion.costo_manutenzione)
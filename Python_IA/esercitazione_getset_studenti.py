# Sistema di gestione studenti
# Immagina di dover creare un sistema di gestione per una scuola che deve
# mantenere le informazioni sugli studenti, i professori e le lezioni.
# Seguendo il paradigma della programmazione orientata agli oggetti (OOP), 
# dovrai implementare le classi necessarie usando incapsulamento, ereditarietà e polimorfismo.

# Specifiche
# Classe Persona:
# Crea una classe base chiamata Persona che rappresenti una persona generica.
# Attributi:
# nome: stringa
# eta: intero
# Metodi:
# init(self, nome, eta): costruttore che inizializza nome ed eta.
# presentazione(self): metodo che stampa una frase con il nome e l'età della persona.
# Regola 1 - Incapsulamento: Gli attributi nome ed eta devono essere privati. Usa getter e setter per accedere e modificare il nome e l'età.
# Classe Studente:
# Crea una sottoclasse di Persona chiamata Studente.
# Attributi:
# voti: lista di interi che rappresentano i voti dello studente.
# Metodi:
# init(self, nome, eta, voti): costruttore che inizializza il nome, l'età e i voti dello studente.
# calcola_media(self): metodo che restituisce la media dei voti.
# Override del metodo presentazione(self) per includere la media dei voti nella presentazione.
# Regola 2 - Ereditarietà: Studente eredita dalla classe Persona.
# Classe Professore:
# Crea una sottoclasse di Persona chiamata Professore.
# Attributi:
# materia: stringa che rappresenta la materia insegnata.
# Metodi:
# init(self, nome, eta, materia): costruttore che inizializza il nome, l'età e la materia insegnata dal professore.
# Override del metodo presentazione(self) per includere la materia nella presentazione.
# Regola 3 - Polimorfismo: Sia la classe Studente che la classe Professore devono fornire una versione specifica del metodo presentazione, rendendolo polimorfico.
class Persona:

    def __init__(self, nome, eta):
        self._nome = nome
        self._eta = eta

    # getter nome
    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valore):
        self._nome = valore

    # getter eta
    @property
    def eta(self):
        return self._eta
    #setter eta
    @eta.setter
    def eta(self, valore):
        self._eta = valore

    # metodo base
    def presentazione(self):
        print("Nome:", self.nome, "- Età:", self.eta)

# Studente che eredita da persona

class Studente(Persona):

    def __init__(self, nome, eta, voti=[]):
        Persona.__init__(self,nome, eta) # fa riferimento a persona
        self.voti =voti

    def calcola_media(self):
        return sum(self.voti) / len(self.voti)
#uso override di presentazione per lo studente
    def presentazione(self):
        print(
            "Nome:", self.nome,
            "- Età:", self.eta,
            "- Media:", self.calcola_media()
        )
        #classe persona
class Professore(Persona):

    def __init__(self, nome, eta, materia):
        Persona.__init__(self,nome, eta)
        self.materia = materia

#uso overryde di presentazione per il professore
    def presentazione(self):
        print("Nome:", self.nome," Età:", self.eta," Materia:", self.materia)

# test
per= Persona("persona", 10)
s = Studente("Peppe", 24, [5, 6, 7, 8])
p = Professore("Michael", 27, "Informatica")
per.presentazione()
s.presentazione()
p.presentazione()
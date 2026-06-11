class Animale:
    def __init__ (self, nome):
        self.nome = nome

    def parla(self):
        print(f"{self.nome} fa suono generico.")

#Classe derivata (eredita da Animale)
class Cane(Animale):
    def parla(self):
        print(f"{self.nome} abbaia!")

        # Output: Fido abbaia!

#create una classe gatto oltre a queste, chiedete all'utente se vuoile creare un gatto o un cane e fatelo parlare
class Gatto(Animale):
    def parla(self):
        print(f"{self.nome} miagola!")


while True:
    scelta=input("vuoi creare un gatto o un cane ")
    animale=None
    if scelta=='gatto':
        nome=input("inserisci nome gatto ")
        animale=Gatto(nome)

    elif(scelta=='cane'):
        nome=input("inserisci nome cane ")
        animale=Cane(nome)

    else:
        print('arrivederci')
        break
    animale.parla()
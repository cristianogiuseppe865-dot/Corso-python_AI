class Studente:
    def __init__(self, nome, voto):
        self.nome = nome
        self._voto = voto # variabile privata (convenzione)

    @property
    def voto(self):
        return self._voto + 1

    @voto.setter
    def voto(self, nuovo_voto):
        if 0 <= nuovo_voto <= 30:
            self._voto = nuovo_voto
        else:
            print("Voto non valido")


pippo = Studente("Pippo",7)
print(pippo.voto)
pippo.voto = 31
print(pippo.voto)
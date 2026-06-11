class Animale:
    def init(self, altezza):
        self.altezza = altezza

    def info(self):
        print(f"Sono alto {self.altezza}")


class Acquatico:
    def init(self, n_pinne):
        self.n_pinne = n_pinne

    def info(self):
        print(f"Hai {self.n_pinne} pinne")


class Pinguino(Acquatico, Animale):
    def init(self, altezza, n_pinne, has_stone=False):
        Animale.init(self, altezza)
        Acquatico.init(self, n_pinne)
        self.has_stone = has_stone

    def info(self):
        print("Sono un pinguino")
        Animale.info(self)


creatura = None
scelta = input("Vuoi creare un pinguino o un animale?")
if scelta=="pinguino":
    creatura = Pinguino(5, 2, True)
else: creatura = Animale(10)

creatura.info()
print(creatura.altezza)
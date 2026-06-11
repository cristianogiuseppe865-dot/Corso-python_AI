class Personaggio:
    def __init__(self, nome, sesso, vita, eta, altezza, danno, fortuna=10):
        self.nome = nome
        self.sesso = sesso
        self.vita = vita
        self.eta = eta
        self.altezza = altezza
        self.danno = danno
        self.fortuna = fortuna

    def attacca(self, nemico):
        nemico.vita -= self.danno
        

class Elfo(Personaggio):
    def __init__ (self, nome, sesso, vita, eta, altezza, danno, mana, danno_magico):
        Personaggio.__init__(self, nome, sesso, vita, eta + 1000, altezza + 5, danno)
        self.mana = mana
        self.danno_magico = danno_magico

    def lancia_magia(self,nemico):
        if(self.mana-2>=0):
            self.mana -= 2
            nemico.vita -= self.danno_magico

class Nano(Personaggio):
    def __init__ (self, nome, sesso, vita, eta, altezza, danno, lancia_asce):
        Personaggio.__init__(self, nome, sesso, vita, eta + 1000, altezza + 5, danno)
        self.lancia_asce = lancia_asce

    def attacca(self, nemico):
        nemico.vita -= (self.danno + self.lancia_asce)


def main():
    print("--- Character Creation ---")
    scelta = input("Choose your class (1: Elf, 2: Dwarf): ")
    nome = input("Enter your name: ")

    # 1. Logic to create the character based on user input
    if scelta == "1":
        player = Elfo(nome, "M", 100, 20, 170, 10, 10, 25)
    else:
        player = Nano(nome, "M", 150, 40, 130, 15, 5)

    # 2. Creating a default character (enemy)
    enemy = Personaggio("Training Dummy", "N/A", 100, 0, 180, 0)

    print(f"\nA wild {enemy.nome} appears!")
    print("-" * 30)

    # 3. Demonstration of inheritance safety
    # We can call .attacca() on 'player' regardless of whether it's an Elf or Dwarf
    # because they both inherit from Personaggio.
    player.attacca(enemy)

    # 4. Using isinstance() for class-specific logic
    if isinstance(player, Elfo): # issubclass() controlla se eredita da
        print(f"{player.nome} is an Elf, so they can use magic!")
        player.lancia_magia(enemy)
    else:
        print(f"{player.nome} is not an Elf; magic is unavailable.")

    print("-" * 30)
    print(f"Final state of {enemy.nome}: {enemy.vita} HP.")

if __name__ == "__main__":
    main()
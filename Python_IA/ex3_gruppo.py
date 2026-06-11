# Ciclo range
# Descrizione: Scrivi un programma che utilizzi un ciclo for con range per
# stampare fino a un massimo N dato dall'utente tramite uno steps dato dall'utente (ES 2 per volta).

numero=int(input("Inserisci numero. "))
steps=int(input("Inserisci intervallo"))
for i in range(0,numero +1,steps):
    print(i)
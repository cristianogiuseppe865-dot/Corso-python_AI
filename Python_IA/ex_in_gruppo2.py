# Descrizione: Scrivi un programma che chieda all'utente
# di inserire una parola e poi utilizzi un ciclo for 
# per stampare ogni lettera della parola su una nuova riga.

parola=input("Inserisci una parola: ")

for lettera in parola:
    print(f"{lettera}\n")
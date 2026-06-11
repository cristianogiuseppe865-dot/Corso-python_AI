# 1.Base / Numeri pari e dispari o sequenza Descrizione:
# Scrivi un programma che chiede all'utente di inserire '
# 'un numero o una stringa scegliendo prima quale. '
# 'Il programma dovrebbe determinare se il numero è pari o dispari '
# 'e stampare il risultato e cheidere all'utente se vuole continuare il ciclo
while True:

    scelta_1 = input("Scegli un operazione: 1.Inserire numero; 2.Inserire stringa ")

    if scelta_1 == "1":

        numero = int(input("Inserisci il numero: "))

        if numero % 2 == 0:
            print("Il numero è pari.")
            print(numero)

        else:
            print("Il numero è dispari.")
            print(numero)

    elif scelta_1 == "2":

        lettera = input("Inserisci la lettera: ")
        print(lettera)

    else:
        print("Scelta non valida")

    scelta_2 = input("Vuoi ripetere? (si/no): ")

    if scelta_2.lower() == "no":
        print("Programma terminato.")
        break
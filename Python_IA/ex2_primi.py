# Chiedi all'utente di inserire un numero.
# Il programma dovrebbe controllare se il numero inserito è primo / pari o no.
#  Se è primo, lo salva e stampa "Il numero è primo". 
# Altrimenti, stampa "Il numero non è primo".
# si ferma il tutto quando ha 5 numeri primi
# lista dove salvo i numeri primi trovati
numeri_primi = []

# il ciclo continua finché non trovo 5 numeri primi
while len(numeri_primi) < 5:

    # chiedo il numero all'utente
    numero = int(input("Inserisci un numero: "))

    # controllo se il numero è pari o dispari
    if numero % 2 == 0:
        print("Il numero è pari")
    else:
        print("Il numero è dispari")

    # i numeri minori di 2 non sono primi
    if numero < 2:
        print("Il numero non è primo")
        continue  # salto al prossimo ciclo

    # variabile per controllare se è primo
    primo = True

    # controllo se il numero ha divisori
    for i in range(2, numero):
        if numero % i == 0:
            primo = False  # trovato un divisore, quindi non è primo
            break

    # se non ho trovato divisori è primo
    if primo:
        print("Il numero è primo")
        numeri_primi.append(numero)  # lo salvo nella lista
    else:
        print("Il numero non è primo")

# quando esco dal ciclo ho trovato 5 numeri primi
print("Ecco i numeri primi inseriti:", numeri_primi)
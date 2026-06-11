# Descrizione: Scrivi un programma che chieda all'utente di inserire due
# numeri e un'operazione da eseguire tra addizione (+), sottrazione (-),
# moltiplicazione (*) e divisione (/). Il programma dovrebbe poi eseguire
# l'operazione e stampare il risultato. Tuttavia, se l'utente tenta di dividere
# per zero, il programma dovrebbe stampare "Errore: Divisione per zero". 

# Se l'operazione inserita non è riconosciuta, dovrebbe stampare "Operazione
# non valida".

numero_1=int(input("Inserisci numero 1 "))
numero_2=int(input("Inserisci numero 2 "))

scelta=int(input("Scegli l'operazione tra: 1.Addizione; 2.Sottrazione; 3.Moltiplicazione; 4.Divisione "))

if scelta == 1:
    somma = numero_1 + numero_2
    print("Il risultato è" , somma)

elif scelta ==2:
    sottrazione = numero_1 - numero_2
    print("Il risultato è" ,sottrazione)

elif scelta ==3:
    moltiplicazione = numero_1 * numero_2
    print("Il risultato  è" , moltiplicazione)

elif scelta ==4:
    if numero_2==0:
        print("Errore divisione per 0")
    else:
        divisione = numero_1 / numero_2
        print("Il risultato è", divisione)
    
else:
    print ("Operazione non valida")
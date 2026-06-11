# 2.Intermedio/ Numeri primi in un intervallo :
# Chiedi all'utente di inserire due numeri che
# definiscono un intervallo (es 10 e 50). 
# Il programma dovrebbe stampare tutti i numeri primi 
# compresi in quell'intervallo o i numeri non primi 
# o entrambi divisi a tua scelta, salvandoli in due aggregazioni differenti 
# e chiedere se deve ripetere
while True:
    numero_1=int(input("Inserisci il primo numero compreso tra 10 e 50: "))
    numero_2=int(input("Inserisci il secondo numero compreso tra 10 e 50: "))
    scelta_1=input("Scegli l'operazione da eseguire: 1.Stampa tutti i numeri primi del range; 2.Stampa tutti i numeri non primi del range ")
    numeri_primi = [11,13,17,19,23,29,31,37,41,43,47]
    numeri_non_primi=[]
    if scelta_1 == "1":
            
        for n in range(numero_1,numero_2 +1):
            if n in numeri_primi:
                print(n)

    elif scelta_1 == "2":

        for non in range(numero_1,numero_2 +1):
            if non not in numeri_primi:
                numeri_non_primi.append(non)   
                print(non)

 
    else:
        print("Scelta non valida")

    scelta_2 = input("Vuoi ripetere? (si/no): ")

    if scelta_2.lower() == "no":
        print("Programma terminato.")
        break

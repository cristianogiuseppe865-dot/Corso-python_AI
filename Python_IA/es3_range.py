# 3.Avanzato/ Fattori comuni Descrizione:

# Chiedi all'utente di inserire due numeri.
# Il programma dovrebbe determinare e stampare i fattori comuni di entrambi i numeri.
# Se non ci sono fattori comuni oltre 1, dovrebbe stampare "I numeri sono coprimi".
n1 = int(input("Primo numero: "))
n2 = int(input("Secondo numero: "))

risultati = []

# Usiamo min() perché un divisore comune non può essere più grande del numero stesso.
for i in range(1, min(n1, n2) + 1):
    
    if n1 % i == 0 and n2 % i == 0:
        risultati.append(i)

# Se dentro è rimasto solo l'1, vuol dire che non hanno altri divisori
if len(risultati) == 1:
    print("I numeri sono coprimi") #definizione coprimo quando appunto l'unico divisore che hanno in comune è 1
else:
    # Altrimenti mostriamo quelli che abbiamo trovato
    print(f"I fattori in comune sono: {risultati}")
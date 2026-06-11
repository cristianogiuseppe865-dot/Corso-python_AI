# 2. Esercizio Avanzato: Sequenza di Fibonacci fino a N Descrizione: 
# Chiedi all'utente di inserire un numero N. '
# 'Il programma dovrebbe stampare la sequenza di Fibonacci fino a N.'
# ' Ad esempio, se l'utente inserisce 100, il programma dovrebbe stampare tutti i numeri 
# della sequenza di Fibonacci minori o uguali a 100.
# Chiediamo il limite  all'utente
n = int(input("Fino a che numero vuoi arrivare? "))

primo = 0
secondo = 1
#La sequenza di Fibonacci è una successione di numeri interi in cui ogni numero (a partire dal terzo) è la somma dei due precedenti.
print("Sequenza:")

while primo <= n:
    
    print(primo)
    
    # 2. Calcola il prossimo numero (somma dei due precedenti)
    prossimo = primo + secondo
    
    # swappo i valori
    primo = secondo
    # Il secondo diventa il nuovo risultato
    secondo = prossimo
#  Punto 4: Utilizzo di if, while e for insieme Scrivi un sistema 
# che prende in input una lista di numeri interi che precedentemente
# è stata valorizzata dall'utente. Il sistema deve:
# 1. Utilizzare un ciclo for per trovare il numero massimo nella lista.
# 2. Utilizzare un ciclo while per contare quanti numeri sono presenti nella lista.
#  3. Utilizzare una condizione if per stampare "Lista Vuota" se la lista è vuota, 
#  altrimenti stampare il numero massimo trovato e il numero di elementi nella lista.

# Chiediamo all'utente quanti numeri vuole inserire
n = int(input("Quanti numeri vuoi inserire? "))

# Creiamo una lista vuota
lista = []

# Inserimento dei numeri nella lista
for i in range(n):
    numero = int(input(f"Inserisci il numero {i + 1}: "))
    lista.append(numero)

# Controllo se la lista è vuota
if len(lista) == 0:
    print("Lista Vuota")
else:
    # Utilizzo del ciclo for per trovare il massimo
    massimo = lista[0] #dando per scontato che il primo sia il massimo

    for numero in lista:
        if numero > massimo:
            massimo = numero

    # contare gli elementi
    conteggio = 0
   
    while conteggio < len(lista):
        conteggio += 1
        
    print("Numero massimo:", massimo)
    print("Numero di elementi:", conteggio)
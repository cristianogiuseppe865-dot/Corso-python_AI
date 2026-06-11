# Punto 3: Utilizzo di for
# Scrivi un sistema che prende in input una lista di numeri e stampa il quadrato di
# ciascun numero nella lista
#numeri da inserire
n = int(input("Quanti numeri vuoi inserire? "))

numeri = []

# Input dei numeri
for i in range(n):
    numero = int(input(f"Inserisci il numero {i + 1}: "))
    numeri.append(numero)

# Stampa dei quadrati
print("\nQuadrati dei numeri inseriti:")

for numero in numeri:
    print(f"{numero}^2 = {numero ** 2}")
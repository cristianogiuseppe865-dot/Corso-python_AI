# Consegna:
# Crea una matrice NumPy 2D di dimensioni 6x6 contenente numeri interi casuali compresi tra 1 e 100.
# Estrai la sotto-matrice centrale 4x4 dalla matrice originale.
# Inverti le righe della matrice estratta (cioè, la prima riga diventa l'ultima, la seconda diventa la penultima, e così via).
# Estrai la diagonale principale della matrice invertita e crea un array 1D contenente questi elementi.
# Sostituisci tutti gli elementi della matrice invertita che sono multipli di 3 con il valore -1.
# Stampa la matrice originale, la sotto-matrice centrale estratta, la matrice invertita, la diagonale principale e la matrice invertita modificata.
# Obiettivo:
# Esercitarsi nell'utilizzo dello slicing di NumPy per estrarre, modificare e manipolare sotto-matrici e array, applicando operazioni avanzate come l'inversione delle righe e la sostituzione condizionale degli elementi.

import numpy as np

# matrice NumPy 2D di dimensioni 6x6 con interi casuali tra 1 e 100

matrice_originale = np.random.randint(1, 101, (6, 6))
print("Matrice: ")
print(matrice_originale)
# sotto-matrice centrale 4x4 dalla matrice originale
sotto_matrice = matrice_originale[1:5, 1:5]


print("Sottomatrice centrale: ")
print(sotto_matrice)



# Inverti le righe della matrice estratta con gli steps a -1
matrice_invertita = sotto_matrice[::-1, :]

print("matrice invertita sulle righe")
print(matrice_invertita)



# Estrai la diagonale principale della matrice invertita e crea un array 1D
diagonale = np.diag(matrice_invertita)

print("diagonale: ")
print(diagonale)



# Sostituisci tutti gli elementi della matrice invertita multipli di 3 con il valore -1

matrice_invertita[matrice_invertita % 3 == 0] = -1

print("matrice invertita multipli di 3 con il valore -1")
print(matrice_invertita)
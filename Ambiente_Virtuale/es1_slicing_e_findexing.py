# Esercizio su NumPy Slicing
# Consegna:
# Crea un array NumPy 1D di 20 numeri interi casuali compresi tra 10 e 50.
# Utilizza lo slicing per estrarre i primi 10 elementi dell'array.
# Utilizza lo slicing per estrarre gli ultimi 5 elementi dell'array.
# Utilizza lo slicing per estrarre gli elementi dall'indice 5 all'indice 15 (escluso).
# Utilizza lo slicing per estrarre ogni terzo elemento dell'array.
# Modifica, tramite slicing, gli elementi dall'indice 5 all'indice 10 (escluso) assegnando loro il valore 99.
# Stampa l'array originale e tutti i sottoarray ottenuti tramite slicing.
# Obiettivo:
# Esercitarsi nell'utilizzo dello slicing di NumPy per estrarre e modificare sottoarray specifici da un array più grande.

import numpy as np


# limite superiore è esclusivo in np.random.randint
array_originale = np.random.randint(10,51,20) # valore piu basso,piu alto e size 

print("Array originale: ", array_originale)

# slicing per estrarre i primi 10 elementi dell'array
primi_dieci = array_originale[:10]
print("Primi 10 elementi: ", primi_dieci)

# 3. gli ultimi 5 elementi dell'array
ultimi_cinque = array_originale[-5:]
print("Ultimi 5 elementi: ", ultimi_cinque)

# 4. Utilizza lo slicing per estrarre gli elementi dall'indice 5 all'indice 15 (escluso)
da_5_a_15 = array_originale[5:15]
print("Elementi dall'indice 5 all'indice 15: ", da_5_a_15)

# ogni terzo elemento dell'array
ogni_terzo = array_originale[2::3]
print("Ogni terzo elemento:\n", ogni_terzo)

#  Modifica, tramite slicing, gli elementi dall'indice 5 all'indice 10 (escluso) assegnando loro il valore 99
array_originale[5:10] = 99
print("Array modificato (con i 99):\n", array_originale)
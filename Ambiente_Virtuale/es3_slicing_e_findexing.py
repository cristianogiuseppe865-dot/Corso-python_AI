# Crea uno script Python che esegua i seguenti passaggi:
# Crea un array NumPy (ndarray) utilizzando np.arange con valori da 0 a 49. più altre 50 posizioni casuali tra 49 e 101.
# Stampa l’array, il suo dtype e la sua shape.
# Modifica il tipo di dato (dtype) dell’array in float64.
# Verifica e stampa di nuovo dtype e shape.
# Utilizza lo slicing per ottenere:
# i primi 10 elementi
# gli ultimi 7 elementi
# gli elementi dall’indice 5 all’indice 20 escluso
# ogni quarto elemento dell'array
# Modifica tramite slicing gli elementi dall’indice 10 a 15 (escluso) assegnando loro il valore 999.
# Utilizza la fancy indexing per selezionare:
# gli elementi in posizione [0, 3, 7, 12, 25, 33, 48]
# tutti gli elementi pari dell’array utilizzando una maschera booleana
# tutti gli elementi maggiori della media dell'array
# Stampa:
# l’array originale dopo tutte le modifiche
# tutti i sotto-array ottenuti tramite slicing e fancy indexin

import numpy as np


# Crea la prima parte dell'array con valori sequenziali da 0 a 49 usando np.arange
parte_sequenziale = np.arange(0, 50)

# Crea la seconda parte con 50 numeri interi casuali tra 49 e 101 (escluso)
parte_casuale = np.random.randint(49, 101, 50)

# fa un append tra la parte casuale alla parte sequenziale creando un unico array
array_originale = np.append(parte_sequenziale, parte_casuale)

# Stampa
print("STATO INIZIALE: ")
print("Array originale:\n", array_originale)
print("Tipo iniziale:", array_originale.dtype)
print("Forma iniziale:", array_originale.shape)

# Modifica il tipo di dato (dtype) dell'array in float64 usando astype
array_originale = array_originale.astype(np.float64)

# Verifica e stampa di nuovo dtype e shape dopo la conversione

print("Nuovo tipo:", array_originale.dtype)
print("Forma attuale:", array_originale.shape)



# Estrae i primi 10 elementi
primi_dieci = array_originale[:10]
print("Primi 10 elementi:\n", primi_dieci)

# Estrae gli ultimi 7 elementi
ultimi_sette = array_originale[-7:]
print("Ultimi 7 elementi:\n", ultimi_sette)

# Estrae gli elementi dall'indice 5 all'indice 20 escluso
da_5_a_20 = array_originale[5:20]
print("Dall'indice 5 a 20 (escluso):\n", da_5_a_20)

# Estrae ogni quarto elemento dell'array
ogni_quarto = array_originale[::4]
print("Ogni quarto elemento:\n", ogni_quarto)




# Modifica tramite slicing gli elementi dall'indice 10 a 15 (escluso) assegnando il valore 999
array_originale[10:15] = 999


# Seleziona gli elementi alle posizioni specificate tramite fancy indexing
indici_specifici = [0, 3, 7, 12, 25, 33, 48]
elementi_selezionati = array_originale[indici_specifici]
print("Elementi alle posizioni [0, 3, 7, 12, 25, 33, 48]:\n", elementi_selezionati)

# Seleziona tutti gli elementi pari dell'array utilizzando una maschera booleana
maschera_pari = (array_originale % 2 == 0)
elementi_pari = array_originale[maschera_pari]
print("Elementi pari dell'array:\n", elementi_pari)

# Calcola la media corrente dell'array per creare la maschera successiva
media_array = np.mean(array_originale)

# Seleziona tutti gli elementi maggiori della media dell'array utilizzando una maschera booleana
maschera_maggiore_media = (array_originale > media_array)
elementi_maggiori_media = array_originale[maschera_maggiore_media]
print(f"Elementi maggiori della media ({media_array:.2f}):\n", elementi_maggiori_media)



# Stampa 
print("ARRAY ORIGINALE DOPO TUTTE LE MODIFICHE: ")
print(array_originale)
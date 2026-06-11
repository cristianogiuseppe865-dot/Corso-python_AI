'''Esercizio Medio: Normalizzazione dei Dati

Testo dell'esercizio:
Creato un DataFrame pandas con tre colonne: altezza, peso e età di un gruppo
di persone, normalizza i dati di altezza e peso usando la normalizzazione min-
max (ridimensiona i valori in modo che varino tra 0 e 1). 
Assicurati di lasciare inalterata la colonna età; mostra il DataFrame
originale e quello modificato.

Fornisci un codice che:
Carichi il DataFrame (puoi assumere che i dati siano già disponibili in un
DataFrame chiamato df).
Applichi la normalizzazione min-max alle colonne altezza e peso.
Stampa sia il DataFrame originale sia quello modificato per compararli.'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# creo il dataframe
a = np.random.randint(150, 200, size=10)
p = np.random.randint(50, 150, size=10)
e = np.random.randint(10, 100, size=10)
dati = {'altezza' : a, 'peso' : p, 'età': e}

df = pd.DataFrame(dati)

# stampo il dataframe
print("---DataFrame---")
print(df)

# normalizzo i valori tra 0 e 1 della colonna altezza
col = df["altezza"] 
df["altezza"] = (col - col.min()) / (col.max() - col.min())

# stampo il dataframe modificato
print("---DataFrame modificato---")
print(df)

# creo la figura che contiene i due grafici
fig,axes = plt.subplots(1, 2, figsize=(12,5))

# creo il primo grafico a barre
sns.barplot(x= df["altezza"], y= df["peso"], ax = axes[0])

# creo il 2 grafico a barre
sns.barplot(x= df["altezza"], y= df["età"], ax = axes[1])

plt.show()
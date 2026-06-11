'''L'obiettivo di questo esercizio è generare un set di dati di serie temporali
utilizzando NumPy, analizzarli con pandas e visualizzare i risultati usando
Matplotlib. Gli studenti dovranno eseguire le seguenti operazioni:


Generazione dei Dati: Utilizzare NumPy per generare una serie temporale
di 365 giorni di dati, simulando il numero di visitatori giornalieri in
un parco. Assumere che il numero medio di visitatori sia 2000 con una
deviazione standard di 500. Inoltre, aggiungere un trend crescente nel
tempo per simulare l'aumento della popolarità del parco.

Creazione del DataFrame: Creare un DataFrame pandas con le date come
indice e il numero di visitatori come colonna.

Analisi dei Dati: Calcolare il numero medio di visitatori per mese e la
deviazione standard.

Visualizzazione dei Dati:

Creare un grafico a linee del numero di visitatori giornalieri.

Aggiungere al grafico la media mobile a 7 giorni per mostrare la
tendenza settimanale.

Creare un secondo grafico che mostri la media mensile dei visitatori.'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# Generazione Dati 
# numero visitatori giornalieri m = 2000 con dev = 500

# Generazione di una serie di date
date_range = pd.date_range(start = '2025-01-01', periods=365, freq='D')
#print(date_range)
numero_visitatori = np.random.normal(loc = 2000, scale = 500, size =365).astype(int)
print(numero_visitatori)
# lasciamo stare per ora il trend crescente

# DataFrame
print('\n')
df_visitatori = pd.DataFrame(numero_visitatori, columns=['Numero_Visitatori'],  index=date_range)
print(df_visitatori)

# Analisi dati raggruppate e filtrate con index.to_period pr mese
statistiche_mensili=df_visitatori.groupby(df_visitatori.index.to_period("M"))["Numero_Visitatori"].agg(
    ["mean", "std"])

# 2 punto finale non svolto insieme al trend crescente
# linspace inizio fine e numero di elementi 

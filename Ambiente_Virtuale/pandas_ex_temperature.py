# Esercizio Facile: Calcolo di Statistiche di Base
# Testo dell'esercizio:
# Hai a disposizione un dataset, che devi autogenerare,
# contenuto in un DataFrame pandas con una singola colonna
# temperature che rappresenta la temperatura giornaliera in
# una città per un mese. 
# Scrivi un programma Python che calcoli e stampi le seguenti
# statistiche:
# La temperatura massima
# La temperatura minima
# La temperatura media
# La mediana delle temperature
import pandas as pd  # importa pandas per gestire il DataFrame
import random  # serve per generare numeri casuali
import matplotlib.pyplot as plt  # libreria per i grafici


# genera 30 temperature casuali tra 15 e 35 gradi
temperature = [random.randint(15, 35) for _ in range(30)]

# crea DataFrame con una colonna
df = pd.DataFrame({'giorno': range(1, 31), 'temperatura': temperature})

max_temp = df['temperatura'].max()  # temperatura massima
min_temp = df['temperatura'].min()  # temperatura minima
media_temp = df['temperatura'].mean()  # media
mediana_temp = df['temperatura'].median()  # mediana

print("MAX:", max_temp)
print("MIN:", min_temp)
print("MEDIA:", round(media_temp, 2))
print("MEDIANA:", mediana_temp)

# 3. LINE PLOT (ANDAMENTO GIORNALIERO)

plt.figure(figsize=(10, 5))  # dimensione grafico

plt.plot(df['giorno'], df['temperatura'])  # linea con punti per ogni giorno

plt.title("Andamento giornaliero temperature")  # titolo grafico
plt.xlabel("Giorno")  # asse X
plt.ylabel("Temperatura")  # asse Y
plt.show()  # mostra grafico

# 4. BOXPLOT (DISTRIBUZIONE)

plt.figure(figsize=(6, 5))  # dimensione grafico

plt.boxplot(df['temperatura'])  # mostra: min, max, mediana, quartili, outlier

plt.title("Boxplot temperature")  # titolo

plt.ylabel("Temperatura")  # asse Y

plt.show()  # mostra grafico
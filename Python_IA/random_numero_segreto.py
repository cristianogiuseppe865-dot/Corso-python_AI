# 1. Esercizio Base: Indovina il numero
# Descrizione: Scrivi un programma che genera un numero casuale tra 1 e 100 (inclusi). 
# L'utente deve indovinare quale numero è stato generato. Dopo ogni tentativo, 
# il programma dovrebbe dire all'utente se il numero da indovinare '
# 'è più alto o più basso rispetto al numero inserito. Il gioco termina '
# 'quando l'utente indovina il numero o decide di uscire. 

#libreria base di python 
import random

# Generiamo il numero casuale tra 1 e 100
numero_segreto = random.randint(1, 100)
tentativo = -1 #per non ottenere casualmente il numero segreto

print("Ho pensato a un numerop tra 1 e 100.")
print("Indovinalo (Digita '0' per arrenderti ed uscire)")

# Il ciclo continua finché l'utente non indovina o non decide di uscire (0)
while tentativo != numero_segreto:
    tentativo = int(input("\nInserisci il tuo tentativo: "))
    
    # Condizione per uscire dal gioco
    if tentativo == 0:
        print(f"Perdente! Il numero era {numero_segreto}. ")
        break
    
    # Controllo del tentativo segreto
    if tentativo == numero_segreto:
        print(f"Complimenti! Hai indovinato, il numero era proprio {numero_segreto}!")
    elif tentativo < numero_segreto:
        print("Il numero da indovinare è più ALTO.")
    else:
        print("Il numero da indovinare è più BASSO.")
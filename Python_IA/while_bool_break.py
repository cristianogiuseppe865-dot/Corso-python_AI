booleano = True # variabile di controllo
counter = 0 # contatore di si

while booleano: # fintanto che la mia variabile è true lui funziona
    a = input("conto quante volte scrivi si: ")
    if a.lower() != "si": # se l'utente scrive qualcosa di divertso da si
# booleano = False # metto bool uguale a false così al prossimo giro si blocca
        break # stoppa del tutto il ciclo
    counter += 1

print(counter) # -1 se si usa la tecnica con il bool dentro l'if
class ContoCorrente:
    # Il saldo=0 nel costruttore lo rende opzionale
    def __init__(self, intestatario, saldo=0):
        self.intestatario = intestatario
        self.saldo = saldo

    def deposita(self, importo):
        # Controllo se l'importo è valido (maggiore di zero)
        if importo > 0:
            self.saldo += importo
            print(f"Deposito di {importo}€ eseguito.")
        else:
            print("Errore: l'importo deve essere positivo.")

    def preleva(self, importo):
        # Controllo se l'importo è disponibile
        if importo > self.saldo:
            print("Errore: Saldo insufficiente.")
        elif importo <= 0:
            print("Errore: l'importo deve essere positivo.")
        else:
            self.saldo -= importo
            print(f"Prelievo di {importo}€ eseguito.")

    def stampa_saldo(self):
        # Metodo per visualizzare lo stato attuale
        print(f"Il saldo di {self.intestatario} è: {self.saldo} €")



# Se non passo il secondo argomento, il saldo sarà 0 automaticamente
mio_conto = ContoCorrente("Gino Rossi") 

while True:
    
    scelta = input("1) Deposita\n2) Preleva\n3) Stampa Saldo\n4) Esci.  ")

    if scelta == "1":
        val = float(input("Quanto vuoi depositare? "))
        mio_conto.deposita(val)
    elif scelta == "2":
        val = float(input("Quanto vuoi prelevare? "))
        mio_conto.preleva(val)
    elif scelta == "3":
        mio_conto.stampa_saldo()
    elif scelta == "4":
        print("Chiusura programma.")
        break
    else:
        print("Scelta non valida.")
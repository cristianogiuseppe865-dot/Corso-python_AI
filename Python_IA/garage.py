# Esercizio 4 (Difficile): 

# Crea una classe chiamata Garage. Questa classe dovrebbe avere:

# Un attributo di istanza capienza (numero massimo di auto) passato al costruttore.

# Un attributo di istanza auto_presenti (lista di stringhe con le targhe), inizialmente vuota.

# Un metodo parcheggia che accetti una targa e aggiunga l'auto alla lista. Se il garage è pieno, stampa un messaggio di errore. Se la targa è già presente, avvisa che l'auto è già in garage.

# Un metodo rimuovi che accetti una targa e rimuova l'auto corrispondente. Se la targa non è presente, stampa un messaggio di errore.

# Un metodo posti_liberi che restituisca il numero di posti ancora disponibili.

# Un metodo statico formato_targa_valido che accetti una stringa e restituisca True se la targa rispetta il formato italiano (2 lettere, 3 numeri, 2 lettere — es. "AB123CD"), False altrimenti. Suggerimento: si può usare il metodo .isalpha() e .isdigit() sulle sottostringhe.

# Il metodo parcheggia deve usare formato_targa_valido per rifiutare targhe non valide prima di aggiungerle.
class Garage:
    # La capienza è fissata a 10 
    def __init__(self):
        self.capienza = 10
        self.auto_presenti = []  

    @staticmethod
    def formato_targa_valido(targa):
       #verufica targa
        if len(targa) != 7:
            return False
        
        #controllo tipi di caratteri
        #is aplpha controlla se i caratteri sono formati da solo lettere
        #is digit controlla se i caratteri sono formati da solo numeri
        
        return (targa[0:2].isalpha() and 
                targa[2:5].isdigit() and 
                targa[5:7].isalpha()) #range per le targe primo numero incluso secondo escluso.

    def posti_liberi(self):
       #posti ancora disponibili
        return self.capienza - len(self.auto_presenti)

    def parcheggia(self, targa):
        targa = targa.upper() #forziamo sempre in maiuscolo
        
        # 1. Verifica formato
        if not Garage.formato_targa_valido(targa):#se la targa è scritta male
            print(f"Formato targa '{targa}' non valido.")
            return

        # 2. Verifica spazio disponibile
        if self.posti_liberi() <= 0:
            print("Garage pieno.")
            return

        # 3. Verifica duplicati
        if targa in self.auto_presenti:
            print(f"L'auto {targa} è già presente nel garage.")
            return

        # 4. Parcheggio
        self.auto_presenti.append(targa)
        print(f"Auto {targa} parcheggiata con successo.")

    def rimuovi(self, targa):
        targa = targa.upper()
        if targa in self.auto_presenti:
            self.auto_presenti.remove(targa)
            print(f"Auto {targa} rimossa correttamente.")
        else:
            print(f"L'auto {targa} non è in questo garage.")




test_garage = Garage()
test_garage.parcheggia("AA123AA")
test_garage.parcheggia("GG5555GG")
test_garage.parcheggia("PP000PP")


while True:
    print(f"\n MENU GARAGE ")
    print("1) Parcheggia")
    print("2) Rimuovi")
    print("3) Mostra auto presenti")
    print("4) Esci")
    
    scelta = input("Cosa vuoi fare? ")

    if scelta == "1":
        targa_input = input("Inserisci la targa: ")
        test_garage.parcheggia(targa_input)

    elif scelta == "2":
        targa_input = input("Inserisci la targa dell'auto da rimuovere: ")
        test_garage.rimuovi(targa_input)

    elif scelta == "3":
        if not test_garage.auto_presenti:
            print("Il garage è attualmente vuoto.")
        else:
            
           print("Auto attualmente in garage:", test_garage.auto_presenti)

    elif scelta == "4":
        print("Chiusura del programma. Arrivederci!")
        break
    else:
        print("Scelta non valida, riprova.")
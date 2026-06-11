class Libro: # dichiaro la classe
    def __init__(self, titolo, autore, numero_pagine): # metodo costruttore
        self.titolo = titolo # attributo di istanza
        self.autore = autore  # attributo di istanza
        self.numero_pagine = numero_pagine 

    def descrizione(self): # metodo di istanza
     
        return f"Il libro '{self.titolo}' è stato scritto da {self.autore} e ha {self.numero_pagine} pagine."

# Creazione del primo libro come oggetto della classe Libro
libro_hp = Libro("Harry Potter e la pietra filosofale", "J.K. Rowling", "304")

# Inizializzo la lista con il primo libro già presente, meglio usare la lista per salvare i vari libri
libri = [libro_hp]

print("Stato iniziale della libreria: ")
print(libri[0].descrizione())

while True:
    scelta = input("\nVuoi inserire un libro? (si/no): ").lower()

    if scelta == "si":
        # Raccogliamo i dati dall'utente
        titolo_user = input("Inserisci il titolo: ")
        autore_user = input("Inserisci l'autore: ")
        pagine_user = input("Inserisci il numero di pagine: ")
        
        # Creiamo l'oggetto e lo aggiungiamo alla lista
        nuovo_libro = Libro(titolo_user, autore_user, pagine_user)
        libri.append(nuovo_libro)
        
        # Stampiamo la lista completa con un ciclo for per averli uno sotto l'altro
        print("\nElenco libri aggiornato: ")
        for libro in libri:
            print(libro.descrizione())
            
    elif scelta == "no":
        print("\nRiepilogo finale: ")
        for libro in libri:
            print(libro.descrizione())
        print("Operazione terminata.")
        break 
    
    else:
        print("Risposta non valida, rispondi con 'si' o 'no'.")
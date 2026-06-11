# Dati iniziali: Crea una lista chiamata prodotti con due elementi: "Mela" e "Banana".

# Prezzi: Crea un dizionario chiamato prezzi dove la chiave è il nome del frutto e il valore è il suo prezzo (es: 0.50 e 0.30).

# L'Input: Chiedi all'utente di inserire l'indice 0 oppure 1.

# Il Ponte: * Recupera il nome del frutto dalla lista usando l'indice inserito.

# Usa quel nome per trovare il prezzo nel dizionario.

# Output: Stampa un messaggio finale tipo: "Hai scelto Mela, il prezzo è 0.50€".

# Lista dei prodotti
lista = ["mela", "banana"]

dizionario = {
    "mela": 0.50,
    "banana": 0.30
}
#scelta utente
scelta = int(input("Inserisci 0 o 1: "))
#recupera il frutto
frutto = lista[scelta]
#recupera il prezzo
prezzo = dizionario[frutto]
#stampa
print("Hai scelto", frutto, "il prezzo è", prezzo, "€")
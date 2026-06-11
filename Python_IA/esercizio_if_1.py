#  Creare una serie di condizioni una dentro l’altra che a fronte di un imput per 
# ogni if decidano se farti passare o no ( 3 livelli, fate un paragone con == )
# Input dell'utente (convertiti in interi)

n1 = int(input("Inserisci il primo numero: "))
n2 = int(input("Inserisci il secondo numero: "))
n3 = int(input("Inserisci il terzo numero: "))

# Primo livello
if n1 == 5:
    print("Primo livello superato")

    # Secondo livello
    if n2 == 10:
        print("Secondo livello superato")

        # Terzo livello
        if n3 == 15:
            print("Hai passato tutti i livelli")
        else:
            print("Terzo livello fallito ")
    else:
        print("Secondo livello fallito ")
else:
    print("Primo livello fallito ")
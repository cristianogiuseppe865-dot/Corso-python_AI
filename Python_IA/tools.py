def numero_primo(n): #sintassi funzione
    if n < 2: 
        print("\nIl numero", n, "non è primo.")
    else:
        primo = True

        for i in range(2, n):
            if n % i == 0:
                primo = False
                break

        if primo:
            print("\nIl numero", n, "è primo.")
        else:
            print("\nIl numero", n, "non è primo.")

def numero_pari(n):
    n = int(input("Inserisci un numero: "))

    if n % 2 == 0:
        print("Il numero è pari.")
    else:
        print("Il numero è dispari.")
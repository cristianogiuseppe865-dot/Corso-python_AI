import random

def genera_numero():
    return random.randint(1, 100)

def chiedi_tentativo():
    scelta = input("\nInserisci un numero tra 1 e 100 (o scrivi 'esci'): ").lower()
    if scelta == 'esci':
        return 'esci'
    return int(scelta) #ovviamente nel caso non ci sia esci

def controlla_numero(segreto, tentativo):
    if tentativo == segreto:
        print("Complimenti! Hai indovinato!")
        return True
    elif tentativo < segreto:
        print("Troppo basso.")
    else:
        print("Troppo alto.")
    return False

def gioca():
    numero_segreto = genera_numero()
    indovinato = False
    
    print("Indovina il numero")
    
    # Ciclo principale: continua finché indovinato è False
    while indovinato==False:
        tentativo = chiedi_tentativo()
        
        # se l'utente vuole uscire
        if tentativo == 'esci':
            print(f"Perdente! Il numero segreto era {numero_segreto}. ")
            break 
            
        # Altrimenti, controlliamo il numero
        indovinato = controlla_numero(numero_segreto, tentativo)


gioca()
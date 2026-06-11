# 3: Gestire una lista di account con username e password,
# permettere all’utente di creare un nuovo account, inserendo uno user e una password, 
# farlo accedere a un messaggio speciale se isnerisce nuovamente i dati in modo corretto 
# (cercate una funzione per controllare che un elemento esista dentro una lista)


# Lista di account username e password
accounts = []

# Creazione nuovo account dell'utente
user = input("Crea username: ")
pwd = input("Crea password: ")
#aggiungi le credenziali alla lista 
accounts.append((user, pwd))
print("Account creato!")

# Login tramite input dell utente
user_login = input("Inserisci username: ")
pwd_login = input("Inserisci password: ")

# Controllo se la coppia username e password esiste nella lista account tramite la funzione in
if (user_login, pwd_login) in accounts:
    print("Accesso riuscito")
else:
    print("Credenziali errate ")
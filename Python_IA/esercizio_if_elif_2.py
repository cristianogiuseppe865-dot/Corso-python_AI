# : Andare a creare un if con vari elif e un else finale che gestisca un menu per la selezione 
# di un crud basilare (aggiungi modifica elimina elementi da una lista) 
lista = ["a", "b", "c"]

scelta = input("Scegli una delle seguenti opzioni dal menu: 1-aggiungi; 2-modifica; 3-elimina; 4-visualizza.1 ")
#scelta operazione aggiungi
if scelta == "1":
    #elemento inserito dall utente e aggiunto alla lista
    x = input("Elemento: ")
    lista.append(x)
    print(lista)
#scelta operazione modifica
elif scelta == "2":
        #elemento modificato dall utente 
    i = int(input("Posizione: ")) -1
    lista[i] = input("Nuovo valore: ")
    print(lista)
#scelta operazione elimina
elif scelta == "3":
        #elemento eliminato dall utente ed eliminato dalla lista

    i = int(input("Posizione: ")) -1
    lista.pop(i)
    print(lista)
#scelta operazione visualizza
elif scelta == "4":
    print(lista)
#printa l'errore
else:
    print("Errore")
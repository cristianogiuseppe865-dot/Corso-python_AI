import random

def inizializza_giocatore():   #statistiche basi del giocatore 
    punti_da_spendere = 10
    attacco = 1
    difesa = 1
    agilita = 1
    
    while (punti_da_spendere) > 0:
        op = int(input("""inserisci cosa vuoi incrementare:
        1) attacco
        2) difesa 
        3) agilità
        > """))   
        # il giocatore sceglie la statistica da migliorare
        if op == 1 : # uprade attacco
            punti_attacco = int(input("inserisci di quanto vuoi aumentare l'attacco > "))
            if punti_attacco <= punti_da_spendere:
                attacco += punti_attacco
                punti_da_spendere -= punti_attacco
            else: 
                print("valore non valido")
                
        elif op == 2: # upgrade difesa
            punti_difesa = int(input("inserisci di quanto vuoi aumentare la difesa > "))
            if punti_difesa <= punti_da_spendere:
                difesa += punti_difesa
                punti_da_spendere -= punti_difesa
            else: 
                print("valore non valido")
        elif op == 3: # upgrade agilita
            punti_agilita = int(input("inserisci di quanto vuoi aumentare l'agilità > "))
            if punti_agilita <= punti_da_spendere:
                agilita += punti_agilita
                punti_da_spendere -= punti_agilita
        else : # in caso venga inserito un numero diverso da 1/2/3
            print("operazione non valida")
    # mostriamo le statistiche dopo i vari upgrade e il nome inserito dal giocatore         
    print(f"attacco = {attacco}, difesa = {difesa}, agilità = {agilita}")
    name = input("inserisci name personaggio > ")
    player = {"name":name,"livello":1,"exp":0,"vitalita":10,"attacco":attacco,"difesa":difesa,"agilità":agilita,"short_rest_remaining":2}
    return player


def initialize_party(): # possibile fare un'espansione per gestire più giocatori
    return [inizializza_giocatore()] #restituisce player come dict

 
def initialize_enemies(): # lista nemici
    return [{"name":"gnome", "vitalita": 5 , "attacco":-1,"difesa":2,"agilità":2},
            {"name":"zombie", "vitalita": 10 , "attacco":1,"difesa":3,"agilità":2},
            {"name":"drago", "vitalita": 15 , "attacco":3,"difesa":5,"agilità":2}]
            
            
def round_print(function): #mostra i dati in input e output 
    def wrapper(entita1,entita2):
        print(f" {entita1['name']} attacca") # Corretto virgolette interne
        damage = function(entita1,entita2)
        print(f" {entita2['name']} riceve {damage}") # Corretto virgolette interne
        return damage
    return wrapper
    


@round_print #ridefinisce la funzione sottostante nella modalità espressa dal raund_print
def attack(giocatore:dict,nemico:dict):
    #la battaglia avviene in contemporanea tra giocatore e nemico
    dado = random.randint(1,6)
    damage = max( ( dado + (giocatore["attacco"] - nemico["difesa"]) ),0) #se è negativo tra () restituisce zero prendendo
    nemico["vitalita"] -= damage
    return damage

def battle(giocatore:dict,nemico:dict): #((giocatore:dict)) serve per fissare il tipo e fornire suggerimenti in fase di stesura del codice
    battle_ended = False
    turno=1
    while not battle_ended:
        print("round ", turno)
        attack(giocatore,nemico)
        attack(nemico,giocatore)

        if giocatore["vitalita"] <= 0 or nemico["vitalita"] <= 0:  #se la vita di uno dei 2 finisce la battle finisce 
            print("battaglia terminata")
            if giocatore["vitalita"] <= 0: # tramite questo if capiamo se vinciamo o perdiamo la battle 
                print("game over")
                exit()
            else:
                print("hai sconfitto "+ nemico["name"])
                battle_ended = True

        print(f"a {giocatore['name'] } rimangono {giocatore['vitalita']} pv")
        input("")
        turno+=1



def handle_login(function):
    def wrapper():
        secret="1234"
        user="gino"
        user_insert=input("Inserisci username: ")
        pass_insert=input("Inserisci password:")

        if user_insert!= user or pass_insert!=secret:
            print("Credenziali invalide")
            return
        function()
    return wrapper  

@handle_login
def game_loop():
    party = initialize_party()
    enemies = initialize_enemies() # lista completa dei nemici
    while enemies: #finchè ci sono nemici da combattere il ciclo continua a girare
        for pg in party:
            print(f"{pg['name']} ha {pg['vitalita'] } pv")
        scelta=int(input("Scegli tra le seguenti operazioni: 1) Affronta il nemico 2) fast rest "))
        nemico=enemies[0]
        if scelta == 1:
        
            print(f"Preparati il {nemico['name']} sta per arrivare") # Corretto virgolette interne
            battle(party[0],nemico)
            enemies.remove(nemico) #rimuovo nemico sconfitto
            
        elif scelta == 2: # gestione del riposo 
                if party[0]["short_rest_remaining"] >= 1 : #se ci sono ancora punti riposo li puoi sfruttare 
                    party[0]["vitalita"] = min(party[0]["vitalita"]+3,10) #la vitalità incrementa di 3 ad ogni riposo
                    print("ti sei riposato.")
                    party[0]["short_rest_remaining"] -= 1 #decrementa i punti riposo che puoi sfruttare
                else:
                    print("non puoi più riposare")
        else:
            print("Operazione non valida")   
    print("Hai vinto")


# Avvio del gioco (chiamata fuori dal loop)
game_loop()
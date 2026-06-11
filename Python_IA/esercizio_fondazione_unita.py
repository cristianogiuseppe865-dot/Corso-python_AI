# # -## Esercitazione: "Neo-City: Il Sistema di Gestione Unità"



# ### Obiettivo

# Sviluppare un prototipo per la gestione delle unità operative in una città futuristica. Dimostrare di saper usare l'**ereditarietà**, il **polimorfismo** (tramite override) e l'**ereditarietà multipla** per creare unità specializzate.



# ---



# ### Task 1: La Fondazione (Ereditarietà Singola)

# Crea una classe base chiamata `Unita`.

# * **Attributi:** `codice_id`, `energia` (0-100).

# * **Metodo `azione()`:** Deve stampare un messaggio generico: *"L'unità [ID] è in attesa di comandi"*.



# Crea poi una sottoclasse `DroneVolante`:

# * **Attributi extra:** `altitudine_max`.

# * **Override di `azione()`:** Deve stampare: *"Il drone [ID] sta effettuando una scansione dall'alto"*.



# ### Task 2: Specializzazione e Polimorfismo

# Crea una classe `RobotOperaio` che eredita da `Unita`.

# * **Attributi extra:** `carico_kg`.

# * **Override di `azione()`:** Deve stampare: *"Il robot [ID] sta sollevando un carico di [carico_kg] kg"*.



# **Esercizio di logica:** Scrivi una funzione `esegui_protocollo(lista_unita)` che prenda una lista contenente droni, operai e unità base, e chiami il metodo `.azione()` su ognuna. Gli studenti devono osservare come ogni oggetto risponda in modo diverso nonostante la chiamata sia la stessa (**Polimorfismo**).



# ---



# ### Task 3: L'Ibrido (Ereditarietà Multipla)

# Qui le cose si fanno interessanti. Supponiamo di avere due classi che definiscono "abilità" specifiche:



# 1. **Classe `ModuloDifesa`:**

# * Metodo `attiva_scudo()`: Stampa *"Scudo energetico attivato!"*.

# 2. **Classe `ModuloRiparazione`:**

# * Metodo `ripara()`: Stampa *"Riparazione dei sistemi in corso..."*.



# Crea la classe **`SentinellaAvanzata`** che eredita da **TUTTE E TRE**: `Unita`, `ModuloDifesa` e `ModuloRiparazione`.



# * La `SentinellaAvanzata` deve poter accedere sia all'energia della classe `Unita`, sia alle funzioni di difesa e riparazione.

# * **Riflessione per la classe:** Cosa succede se sia `Unita` che `ModuloDifesa` avessero un metodo con lo stesso nome? (Introduzione al concetto di **MRO - Method Resolution Order**).







# ---



# ### Task 4: Il Test Finale (Main)

# Scrivi un programma che:

# 1. Istanzia un `DroneVolante` e un `RobotOperaio`.

# 2. Istanzia una `SentinellaAvanzata`.

# 3. Usa `isinstance()` per verificare se la `SentinellaAvanzata` è effettivamente un'istanza di `Unita`.

# 4. Fai compiere alla Sentinella tutte le sue azioni: deve presentarsi (azione), difendersi e ripararsi.



# ---



# ### Bonus Challenge (Per i più veloci)

# Aggiungi un controllo nel metodo `azione()`: se l'energia è sotto il 10%, l'unità non può eseguire l'azione e deve stampare *"Energia insufficiente"*. Come cambierebbe il comportamento della `SentinellaAvanzata` che eredita da più moduli?

class Unita:
    def __init__(self, codice_id, energia=100):
        self.codice_id = codice_id
        self.energia = energia

    def azione(self):
        # Bonus Challenge: Controllo energia
        if self.energia < 10:
            print(f"[{self.codice_id}] ERRORE: Energia insufficiente ({self.energia}%)")
        else:
            print(f"L'unità {self.codice_id} è in attesa di comandi.")

class DroneVolante(Unita):
    def __init__(self, codice_id, energia, altitudine_max):
        # Richiamiamo il costruttore della classe base
        super().__init__(codice_id, energia)
        self.altitudine_max = altitudine_max

    def azione(self):
        if self.energia < 10:
            super().azione() # Sfrutta il controllo energia della classe base
        else:
            print(f"Il drone {self.codice_id} sta effettuando una scansione dall'alto (Alt: {self.altitudine_max}m)")

class RobotOperaio(Unita):
    def __init__(self, codice_id, energia, carico_kg):
        super().__init__(codice_id, energia)
        self.carico_kg = carico_kg

    def azione(self):
        if self.energia < 10:
            super().azione()
        else:
            print(f"Il robot {self.codice_id} sta sollevando un carico di {self.carico_kg} kg")

# Esercizio di logica: Polimorfismo
def esegui_protocollo(lista_unita):
    print("\n--- AVVIO PROTOCOLLO OPERATIVO ---")
    for u in lista_unita:
        # Chiamiamo lo stesso metodo su oggetti diversi
        u.azione()

# --- TASK 3: L'Ibrido (Ereditarietà Multipla) ---

class ModuloDifesa:
    def attiva_scudo(self):
        print("Scudo energetico attivato!")

class ModuloRiparazione:
    def ripara(self):
        print("Riparazione dei sistemi in corso...")

# La Sentinella eredita da 3 classi diverse
class SentinellaAvanzata(Unita, ModuloDifesa, ModuloRiparazione):
    def azione(self):
        if self.energia < 10:
            super().azione()
        else:
            print(f"Sentinella {self.codice_id}: Sistemi attivi. Monitoraggio perimetro in corso.")

# --- TASK 4: Il Test Finale (Main) ---

if __name__ == "__main__":
    # 1. Istanziamo le unità
    drone = DroneVolante("DRN-500", 80, 150)
    operaio = RobotOperaio("WRK-10", 95, 500)
    # Creiamo un'unità con energia bassa per testare il Bonus
    operaio_scarico = RobotOperaio("WRK-X", 5, 200) 
    
    # 2. Istanziamo la Sentinella Avanzata
    sentinella = SentinellaAvanzata("SNT-ULTRA", 100)

    # 3. Verifica istanza
    print(f"La sentinella è un'unità base? {isinstance(sentinella, Unita)}")

    # 4. Test Polimorfismo
    unita_citta = [drone, operaio, operaio_scarico, sentinella]
    esegui_protocollo(unita_citta)

    # 5. Test abilità uniche della Sentinella
    print(f"\n--- Test Sistemi Sentinella {sentinella.codice_id} ---")
    sentinella.attiva_scudo()  # Da ModuloDifesa
    sentinella.ripara()        # Da ModuloRiparazione
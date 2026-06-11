## Estendere una classe base UnitaMilitare per creare diverse unità specializzate, ciascuna con compiti e metodi specifici. 
# Inoltre, implementare una classe ControlloMilitare che eredita da tutte le altre classi
# per gestire e tenere traccia delle diverse unità. Utilizzando tutti i metodi speciali.

## Classe UnitaMilitare:
# Attributi:
# nome (stringa): nome dell'unità.
# numero_soldati (intero): numero di soldati nell'unità.
#Metodi:
# muovi(): stampa un messaggio sul movimento dell'unità.
# attacca(): stampa un messaggio sull'attacco.
# ritira(): gestisce il ritiro strategico.
# Classi Derivate:
# Fanteria:
# costruisci_trincea(): costruisce difese temporanee.
# Artiglieria:
# calibra_artiglieria(): calibra i pezzi di artiglieria per la precisione.
# Cavalleria:
# esplora_terreno(): esplora l'area per raccogliere informazioni sul nemico.
# SupportoLogistico:
# rifornisci_unita(): gestisce il rifornimento e la manutenzione.
# Ricognizione:
# conduci_ricognizione(): conduce missioni di sorveglianza.
# Classe ControlloMilitare:
# Eredita da tutte le classi precedenti.
# Attributi aggiuntivi:
# unita_registrate: dizionario/due liste per tenere traccia delle unità create.
# Metodi:
# registra_unita(unita): aggiunge un'unità al registro.
# mostra_unita(): elenca tutte le unità registrate.
# dettagli_unita(nome): mostra dettagli specifici di un'unità.
# =============================================================================
# CLASSE BASE: UnitaMilitare
# =============================================================================
class UnitaMilitare:
    """
    Questa è la classe 'Madre'. Definisce le fondamenta per ogni unità.
    Utilizziamo il metodo speciale __init__ per costruire l'oggetto e 
    __str__ per rappresentarlo come stringa.
    """
    def __init__(self, nome, numero_soldati):
        # Inizializzazione degli attributi base
        self.nome = nome
        self.numero_soldati = numero_soldati

    def muovi(self):
        print(f" LOGISTICA: L'unità {self.nome} sta avanzando sul terreno.")

    def attacca(self):
        print(f" COMBATTIMENTO: L'unità {self.nome} ha ingaggiato il nemico!")

    def ritira(self):
        print(f" TATTICA: L'unità {self.nome} effettua un ripiegamento strategico.")

    def __str__(self):
        """Metodo speciale: definisce cosa appare quando scriviamo print(oggetto)."""
        return f"[Unità: {self.nome} | Effettivi: {self.numero_soldati}]"

    def __len__(self):
        """Metodo speciale: permette di usare len(unita) per ottenere il numero di soldati."""
        return self.numero_soldati


# =============================================================================
# CLASSI DERIVATE (SPECIALIZZAZIONI)
# =============================================================================
# Ognuna di queste classi eredita da UnitaMilitare (Ereditarietà Singola)

class Fanteria(UnitaMilitare):
    def costruisci_trincea(self):
        print(f" DIFESA: {self.nome} sta scavando fortificazioni temporanee.")

class Artiglieria(UnitaMilitare):
    def calibra_artiglieria(self):
        print(f" PRECISIONE: {self.nome} sta impostando gli alzi per i cannoni.")

class Cavalleria(UnitaMilitare):
    def esplora_terreno(self):
        print(f" ESPLORAZIONE: {self.nome} sta mappando i punti ciechi del nemico.")

class SupportoLogistico(UnitaMilitare):
    def rifornisci_unita(self):
        print(f" RIFORNIMENTO: {self.nome} sta distribuendo munizioni e razioni.")

class Ricognizione(UnitaMilitare):
    def conduci_ricognizione(self):
        print(f" SORVEGLIANZA: {self.nome} sta raccogliendo dati sensibili (Stealth).")


# =============================================================================
# CLASSE DI CONTROLLO: ControlloMilitare
# =============================================================================
class ControlloMilitare(Fanteria, Artiglieria, Cavalleria, SupportoLogistico, Ricognizione):
    """
    Questa classe utilizza l'EREDITARIETÀ MULTIPLA. 
    Ereditando da tutte, ha tecnicamente accesso a tutti i loro metodi.
    Gestisce un registro interno di tutte le unità create nel sistema.
    """
    def __init__(self):
        # Usiamo un dizionario per tenere traccia delle unità: Nome -> Oggetto
        self.unita_registrate = {}

    def registra_unita(self, unita):
        """Aggiunge un oggetto unità al dizionario del comando."""
        self.unita_registrate[unita.nome] = unita
        print(f" SISTEMA: Unità '{unita.nome}' inserita nel registro centrale.")

    def mostra_unita(self):
        """Cicla nel registro e mostra tutte le unità registrate."""
        print("\n" + "="*30)
        print(" ELENCO FORZE AL COMANDO ")
        print("="*30)
        for unita in self.unita_registrate.values():
            print(unita) # Qui agisce il metodo __str__ di UnitaMilitare

    def dettagli_unita(self, nome):
        """Cerca un'unità specifica per nome e ne mostra i dettagli."""
        unita = self.unita_registrate.get(nome)
        if unita:
            print(f"\n--- DETTAGLI SPECIFICI PER {nome} ---")
            print(f"Stato: Operativa")
            print(f"Soldati al fronte: {len(unita)}") # Qui agisce il metodo __len__
        else:
            print(f"\n ERRORE: L'unità '{nome}' non risulta registrata.")


# =============================================================================
# ESECUZIONE DEL TEST (MAIN)
# =============================================================================
if __name__ == "__main__":
    # 1. Creiamo il Centro di Comando
    comando_centrale = ControlloMilitare()

    # 2. Creiamo le varie unità specializzate
    alfa = Fanteria("Brigata Alpina", 120)
    beta = Artiglieria("Batteria Tuono", 45)
    gamma = Ricognizione("Ombra-1", 12)

    # 3. Registrazione presso il comando
    comando_centrale.registra_unita(alfa)
    comando_centrale.registra_unita(beta)
    comando_centrale.registra_unita(gamma)

    # 4. Visualizzazione globale
    comando_centrale.mostra_unita()

    # 5. Esecuzione azioni specifiche (Polimorfismo)
    print("\n--- OPERAZIONI SUL CAMPO ---")
    alfa.costruisci_trincea()      # Metodo specifico Fanteria
    beta.calibra_artiglieria()     # Metodo specifico Artiglieria
    gamma.conduci_ricognizione()   # Metodo specifico Ricognizione

    # 6. Esecuzione metodi base ereditati
    alfa.muovi()
    beta.attacca()
    gamma.ritira()

    # 7. Dettagli finali tramite il controllo centrale
    comando_centrale.dettagli_unita("Brigata Alpina")
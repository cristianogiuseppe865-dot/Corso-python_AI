# creare una classe base MetodoPagamento e diverse classi derivate che rappresentano diversi metodi di pagamento.
# Questo scenario permetterà di vedere il polimorfismo in azione, permettendo alle diverse sottoclassi di implementare 
# i loro specifici comportamenti di pagamento, pur aderendo all'interfaccia comune definita dalla classe base.

# Classe MetodoPagamento:
# Metodi:
# effettua_pagamento(importo): un metodo che ogni sottoclasse dovrà implementare.
# Classi Derivate:
# CartaDiCredito:
# Metodi come effettua_pagamento(importo) che simula un pagamento tramite carta di credito.
# PayPal:
# Metodi come effettua_pagamento(importo) che simula un pagamento tramite PayPal.
# BonificoBancario:
# Metodi come effettua_pagamento(importo) che simula un pagamento tramite bonifico bancario.
# GestorePagamenti:
# Una classe che usa un'istanza di MetodoPagamento per effettuare pagamenti, senza preoccuparsi del dettaglio del metodo di pagamento.

#CLASSE BASE 
class MetodoPagamento:
    def effettua_pagamento(self, importo, saldo_attuale):
        # Questo messaggio apparirà solo se la sottoclasse NON definisce il suo metodo
        print("ATTENZIONE: Metodo di pagamento generico, nessuna azione eseguita.")
        return saldo_attuale

#CLASSI DERIVATE 
class CartaDiCredito(MetodoPagamento):
    def effettua_pagamento(self, importo, saldo_attuale):
        print(f"\n Transazione CARTA DI CREDITO ")
        if saldo_attuale >= importo:
            nuovo_saldo = saldo_attuale - importo
            print(f"Pagamento di {importo}€ approvato.")
            return nuovo_saldo
        else:
            print("Errore: Fondi sulla carta insufficienti!")
            return saldo_attuale

class PayPal(MetodoPagamento):
    def effettua_pagamento(self, importo, saldo_attuale):
        print(f"\n Transazione PAYPAL ")
        if saldo_attuale >= importo:
            nuovo_saldo = saldo_attuale - importo
            print(f"Login effettuato. {importo}€ inviati con successo.")
            return nuovo_saldo
        else:
            print("Errore: Saldo PayPal insufficiente!")
            return saldo_attuale

#GESTORE 
class GestorePagamenti:
    def esegui_ordine(self, metodo, importo, saldo):
        # Il gestore chiama il metodo e riceve indietro il saldo aggiornato
        nuovo_saldo = metodo.effettua_pagamento(importo, saldo)
        print(f"Saldo residuo dopo l'operazione: {nuovo_saldo}€")
        return nuovo_saldo

#TEST PRATICO 
gestore = GestorePagamenti()
mio_saldo = 100.0  # Partiamo con 100 euro

# 1. Paghiamo con Carta (Scaliamo 30)
mio_saldo = gestore.esegui_ordine(CartaDiCredito(), 30.0, mio_saldo)

# 2. Paghiamo con PayPal (Scaliamo 50)
mio_saldo = gestore.esegui_ordine(PayPal(), 50.0, mio_saldo)

# 3. Tentativo di acquisto troppo costoso (40)
mio_saldo = gestore.esegui_ordine(CartaDiCredito(), 40.0, mio_saldo)
# Esercizio 1 (Facile):

# Crea una classe chiamata Punto. 

# Questa classe dovrebbe avere:

# Due attributi: x e y, per rappresentare le coordinate del punto nel
# piano.

# Un metodo muovi che prenda in input un valore per dx e un valore
# per dy e modifichi le coordinate del punto di questi valori.

# Un metodo distanza_da_origine che restituisca la distanza del punto
# dall'origine (0,0) del piano.


class Punto:
    def __init__(self, x, y):
        # Assegniamo le coordinate iniziali
        self.x = x
        self.y = y
  
    def muovi(self, dx, dy):
        # Sommiamo lo spostamento alle coordinate attuali
        self.x += dx
        self.y += dy
   
    def distanza_da_origine(self):
        # Calcoliamo la distanza con il Teorema di Pitagora:
        # radice quadrata di (x^2 + y^2)
        # Usiamo ** 0.5 per fare la radice quadrata semplificando l'operazione
        distanza = (self.x**2 + self.y**2) ** 0.5 #** elevazione 
        return distanza


p = Punto(6, 8)

print(f"Punto creato in: ({p.x}, {p.y})")
print(f"Distanza: {p.distanza_da_origine()}") # Dovrebbe dare 10.0

p.muovi(-3, -4)
print(f"Dopo il movimento: ({p.x}, {p.y})")
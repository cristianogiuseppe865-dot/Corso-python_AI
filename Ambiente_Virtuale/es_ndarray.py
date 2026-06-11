
# Crea un array NumPy utilizzando arange e verifica il tipo di dato (dtype) e la forma (shape) dell'array.
# Esercizio:
# Utilizza la funzione np.arange per creare un array di numeri interi da 10 a 49.
# Verifica il tipo di dato dell'array e stampa il risultato.
# Cambia il tipo di dato dell'array in float64 e verifica di nuovo il tipo di dato.
# Stampa la forma dell'array.
# Importa la libreria numpy con l'alias np
import numpy as np


# Utilizza la funzione np.arange per creare un ndarray di numeri interi da 10 a 49
array = np.arange(10, 50)

# Stampa l'array originale a schermo
print("Array: ",array)

# Verifica il tipo di dato (dtype) dell'array originale e stampa il risultato
print("Tipo: ",array.dtype)

# Stampa la forma (shape) dell'array originale
print("Forma: ",array.shape)



# Cambia solo il tipo di dato dell'array in float64 senza modificarne la forma
array_float = array.astype(np.float64)

# Stampa il nuovo array modificato a schermo
print("Nuovo array: ",array_float)

# Verifica di nuovo il tipo di dato (dtype) dopo il cambiamento
print("Nuovo tipo: ",array_float.dtype)

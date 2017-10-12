#Importamos funciones de la libreria standar que se llama random
import random

# 1. Lista con frases en aleman
# 2. Generar un numero aleatorio
# 3. Imprimir la entrada de la lista con indice obtenido en el paso 2

# Primera lista de frases:
frases_aleman = ["ich hoffe es auch", "frisch verheiratet", "das Mittelalter", "ich weiss es noch nicht", "es hängt davon ab", "insgesamt", "über den Kopf", "immer noch", "Das läuft uns nicht weg"]


indice = random.randint (0, len (frases_aleman) -1)

print (frases_aleman[indice])

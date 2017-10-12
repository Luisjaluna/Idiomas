#Importamos funciones de la libreria standar que se llama random
import random

# 1. Lista con otras cosas de aleman
# 2. Generar un numero aleatorio
# 3. Imprimir la entrada de la lista con indice obtenido en el paso 2


# Primera lista de otras cosas de palabras:
otros_aleman = ["daran", "sogar", "debei", "da", "nun", "längst", "Alltag", "miteinander", "allerdings", "der Feierabend", "der Studentenausweis", "die Erziehung", "die Kneipe", "die Beerdigung", "das Missverständnis", "das lexikon", "der Umgang", "die Behandlung", "der Ausnahmezustand", "falls"]



indice = random.randint (0, len (otros_aleman) -1)

print (otros_aleman[indice])

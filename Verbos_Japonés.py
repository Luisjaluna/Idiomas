#Importamos funciones de la libreria standar que se llama random
import random

# 1. Lista con verbos en japones
# 2. Generar un numero aleatorio
# 3. Imprimir la entrada de la lista con indice obtenido en el paso 2

# Primera lista de palabras palabras:
verbos_japones = ["okimasu", "nemasu", "hatarakimasu", "yasumimasu", "benkyoshimasu", "owarimasu"]


indice = random.randint (0, len (verbos_japones) -1)

print (verbos_japones[indice])

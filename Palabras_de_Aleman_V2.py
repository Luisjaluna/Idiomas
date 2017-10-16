#Importamos funciones de la libreria standar que se llama random
import random

# 1. Lista con verbos en aleman
# 2. Generar un numero aleatorio
# 3. Imprimir la entrada de la lista con indice obtenido en el paso 2


# Primera lista de verbos:
verbos_aleman = ["besuchen", "besichtigen", "schicken", "zergehen ", "lassen", "umblättern", "unterkriegen", "wühlen", "einfallen", "weg gelaufen","verwechseln", "bestehen", "beschuldigen", "erholen", "schnipsen", "klatschen", "nicken", "schütteln", "fragen stellen", "stören","schelten", "überzeugen", "zeugen", "beitragen", "mixen", "ausrufen", "verlieren", "umziehen", "bedrohen", "versprechen", "lächeln", "lachen", "nennen", "kümmern", "schimpfen", "umdenken", "ernähren", "betteln","betreffen", "wirken", "öffnen", "vorschlagen", "nachdenken", "wachsen", "anschauen", "auskommen", "überzogen", "rühren", "achten", "begründen", "aufkommen", "aussehen", "anfangen", "erklären", "berichten über", "vergessen", "sich gewöhnen","wählten" ]

while True:

	indice = random.randint (0, len (verbos_aleman) -1)

	print (verbos_aleman[indice])
	
	input ("Presiona Enter para una nueva palabra:")

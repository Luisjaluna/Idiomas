#Importamos funciones de la libreria standar que se llama random
import random

# 1. Lista con palabras en aleman
# 2. Generar un numero aleatorio
# 3. Imprimir la entrada de la lista con indice obtenido en el paso 2

"""
# Primera lista de palabras palabras:
palabras_aleman = ["das Mittlehrealter", "der Vorwurf", "der Ausdruck", "das Geräusch", "der Ton", "das Tor", "die Ablehnung", "die Einstellung", "das Ereignis", "der Feierabend", "der Studentenausweis", "die Erziehung", "die Kneipe", "die Beerdigung", "das Missverständnis", "das lexikon", "der Umgang", "die Behandlung", "der Ausnahmezustand", "der Kreislauf", "das Röhrchen", "die Strafe", "die Anzeige", "die Spende", "der Bettler", "der Blitz", "der Donner", "Sturmfluten", "Sorgen","Gedanke", "Betracht", "Vortrag", "sich gewöhnen", "Plakat", "die Einleitung", "die Wahl", "die Gestaltung", "Möglichkeiten", "Bewerbung", "das Spaß", "die Erwähnung", "wählten", ]
"""

# Primera lista de palabras palabras:
palabras_aleman = ["die Erziehung", "der Umgang", "die Behandlung", "die Strafe", "die Anzeige", "die Spende", , "Betracht", "Vortrag", "Plakat", "die Einleitung", "die Wahl", "die Gestaltung", "Möglichkeiten", "Bewerbung", "das Spaß", "die Erwähnung"]

indice = random.randint (0, len (palabras_aleman) -1)

print (palabras_aleman[indice])




























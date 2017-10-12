#Importamos funciones de la libreria standar que se llama random
import random

# 1. Lista con adjetivos en aleman
# 2. Generar un numero aleatorio
# 3. Imprimir la entrada de la lista con indice obtenido en el paso 2

# Primera lista de adjetivos:
adjetivos_aleman = ["schlimm", "energiegeladen", "vulgär", "farbig", "liebevoll", "alkoholhaltig", "stur", "unschuldig", "schleimig", "fettig","unterhaltsam", "spontan", "altmodisch", "bunt", "öffentliche", "unangebracht", "unpassend", "enge", "passend", "empfindlich","unwohl", "grundlegend", "gesundheitliche", "ähnlich", "schlimm", "ungewöhnlich", "wach", "fleckig", "gesamt",  ]


indice = random.randint (0, len (adjetivos_aleman) -1)

print (adjetivos_aleman[indice])

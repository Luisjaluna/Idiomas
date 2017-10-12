#Importamos funciones de la libreria standar que se llama random
import random

# 1. Lista con palabras en japones
# 2. Generar un numero aleatorio
# 3. Imprimir la entrada de la lista con indice obtenido en el paso 2

# Primera lista de palabras palabras:
palabras_japones = ["ame", "ao", "ie", "e", "uma", "ue", "aka", "kao", "eki", "koe","asa", "kasa", "ashi", "ishi", "shio", "sushi", "suika", "sekai", "soto", "kata","shita", "kuchi", "tsukue", "te", "tokei", "natsu", "kuni", "niku", "sakana", "kinou","inu", "neko", "nori", "hana", "haha", "ha", "hito", "hikouki", "fune", "hoshi","machi", "mame", "umi", "mimi", "kami", "mushi", "me", "momo", "kimono", "yama","heya","yuki", "yume", "yoyaku", "sora", "tori", "yoru", "kuro", "shiro", "furo", "rekishi","tonari", "sakura", "kawa", "hon", "kin", "mikan", "kagi", "eigo", "nihongo", "ringo", "nihonjin", "kaze", "kazoku", "daigaku", "ichigo", "denwa", "mado", "kubi", "yubi", "shinbun", "boushi", "kyonen", "isha", "shashin", "jidousha", "toshokan", "juu", "hyaku", "byouin", "gyuunyuu", "zasshi", "gakkou"]

# Segunda lista de palabras palabras:
	#palabras_japones = []



indice = random.randint (0, len (palabras_japones) -1)

print (palabras_japones[indice])



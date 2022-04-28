from imagesearch import *
from pyautogui import *
from dokkanlibrary import *




#Encontrar zona a completar
print("~~~ DOKKAN BOT INITIALIZED - (BETA-0.1) ~~~")
x = 1
niveles_completados = 0
while x == 1:
	print("Se han completado "+str(niveles_completados)+" niveles.")
	z = first_locator()
	restart = complete(z[0],z[1],z[2])
	if restart == True:
		continue
	time.sleep(4)
	cambia_completado(z[0],z[1],z[2],True)
	print("Nivel marcado como completado, buscando siguiente nivel.")
	niveles_completados = niveles_completados+1
	time.sleep(16)


from dokkanlibrary import *
from ast import *
from imagesearch import *
from pyautogui import *
from threading import *


img_quest = "img/quest.png"
img_area_highlighted = "img/area_highlighted.png"
img_zona_highlighted = "img/zona_highlighted.png"
img_normal = "img/normal.png"
img_hard = "img/hard.png"
img_z_hard = "img/z_hard.png"
img_super = "img/super.png"
img_friend = "img/friend.png"
img_start = "img/start.png"
img_ok = "img/ok.png"
img_skip = "img/skip.png"
img_cancel = "img/cancel.png"
img_battle = "img/battle.png"
img_K = "img/k.png"
img_stone = "img/stone.png"
img_home = "img/home.png"
img_item = "img/item.png"
img_1 = "img/1.png"
img_2 = "img/2.png"
img_3 = "img/3.png"
img_4 = "img/4.png"
img_5 = "img/5.png"
img_6 = "img/6.png"
img_up = "img/up.png"
img_down = "img/down.png"
img_left = "img/left.png"
img_right = "img/right.png"
img_battle = "img/battle.png"
img_lvl = "img/lvl.png"
PH12 = True

"""
completado()
imputs:
cleared = la ruta del archivo donde se guardan los datos. por default es "cleared.txt".
area = Area desde la 1 hasta la 27.
zona = Zona desde la 1 hasta la 3/5/8/10 dependiendo del nivel.
dificultad= Dificultad desde la 1 hasta la 3.
output:
True si esta completado. False si no esta completado.
"""

def completado(area,zona,dificultad,cleared="cleared.txt"):
	o = open(cleared,"r")
	r = o.read()
	l = literal_eval(r)
	area = int(area)
	zona = int(zona)
	dificultad = int(dificultad)
	clearedtruefalse = l[area][zona][dificultad]
	return clearedtruefalse
	
	
	
def cambia_completado(area,zona,dificultad,valor,cleared="cleared.txt"):
	o = open(cleared,"r")
	r = o.read()
	l = literal_eval(r)
	area = int(area)
	zona = int(zona)
	dificultad = int(dificultad)
	o.close()
	o = open(cleared,"w")
	l[area][zona][dificultad] = valor
	s = str(l)
	o.write(s)
	o.close()
	
"""
firstlocator()
output:
Lista con 3 elementos: [Area, Zona, Dificultad]
"""
	
def first_locator():
	area = 1
	zona = 1
	dificultad = 1
	placeholder=1
	while placeholder == 1:
		try:
			if completado(area,zona,dificultad) == False:
				print("Area encontrada: Area "+str(area)+",zona "+str(zona)+",dificultad "+str(dificultad)+".")
				break
			elif dificultad != 3:
				dificultad = dificultad+1
				continue
			elif placeholder ==1:
					dificultad = 1
					zona = zona+1
					continue
		except:
			area = area+1
			zona = 1
			if area != 28:
				continue
			else:
				print("SUCCESS! Todos los niveles completados.")
				area = 0
				zona = 0
				dificultad = 0
				break
	listacoords = [area,zona,dificultad]
	return listacoords
	
"""
complete()
imputs:
area = Area desde la 1 hasta la 27.
zona = Zona desde la 1 hasta la 3/5/8/10 dependiendo del nivel.
dificultad = dificultad= Dificultad desde la 1 hasta la 3.
"""

def complete(area,zona,dificultad):
	#Variables imagenes

	
	
	#Entrar al nivel
	coords_quest = imagesearch_loop(img_quest,0.01) #el primer num es x, el segundo y, y si es -1 no esta en la pantalla
	click_image(img_quest,coords_quest,"left",0.5)
	print("Entrando al menu area")
	
	#Seleccion de area
	
	time.sleep(3)
	coords_area_highlighted = imagesearch_loop(img_area_highlighted,0.01)
	
	scrolldown = 0
	while scrolldown <= 28:
		scroll(-100)
		scrolldown = scrolldown +1
		time.sleep(0.2)
		continue
	scrollup = 0
	while scrollup != area-1:
		scroll(100)
		scrollup = scrollup +1
		time.sleep(0.2)
		continue
	click_image(img_area_highlighted,coords_area_highlighted,"left",0.2)
	
	
	coords_zona_highlighted = imagesearch_loop(img_zona_highlighted,0.01,0.99)
	time.sleep(0.7)
	
	print("Entrando al menu zona")
	
	scrolldown = 0
	while scrolldown <= 10:
		scroll(-100)
		scrolldown = scrolldown +1
		time.sleep(0.2)
		continue
	scrollup = 0
	while scrollup != zona-1:
		scroll(100)
		scrollup = scrollup +1
		time.sleep(0.2)
		continue
	click_image(img_zona_highlighted,coords_zona_highlighted,"left",0.2)
	
	print("Entrando al menu dificultad")
	
	#Si el area es 19 o mas cambian las dificultades
	time.sleep(6)
	
	if area <= 18:
		if dificultad == 1:
			coords_normal = imagesearch_loop(img_normal,0.01)
			click_image(img_normal,coords_normal,"left",0.2)
		
		elif dificultad == 2:
			coords_hard = imagesearch_loop(img_hard,0.01)
			click_image(img_hard,coords_hard,"left",0.2)
		
		else:
			coords_z_hard = imagesearch_loop(img_z_hard,0.01)
			click_image(img_z_hard,coords_z_hard,"left",0.2)
			time.sleep(5)
			coords_ok = imagesearch(img_ok,0.7)
			if coords_ok[0] != -1:
				click_image(img_ok,coords_ok,"left",0.2)
	else:
		if dificultad == 1:
			coords_hard = imagesearch_loop(img_hard,0.01)
			click_image(img_hard,coords_hard,"left",0.2)
		
		elif dificultad == 2:
			coords_z_hard = imagesearch_loop(img_z_hard,0.01)
			click_image(img_z_hard,coords_z_hard,"left",0.2)
		
		else:
			coords_super = imagesearch_loop(img_super,0.01)
			click_image(img_super,coords_super,"left",0.2)
			time.sleep(8)
			coords_ok = imagesearch(img_ok,0.7)
			if coords_ok[0] != -1:
				click_image(img_ok,coords_ok,"left",0.2)
			
	time.sleep(5)
	coords_ok = imagesearch(img_ok)
	if coords_ok[0] != -1:
		click_image(img_ok,coords_ok,"left",0.2)
		time.sleep(3)
		coords_ok = imagesearch(img_ok)
		click_image(img_ok,coords_ok,"left",0.2)
		time.sleep(5)
		coords_home = imagesearch(img_home)
		click_image(img_home,coords_home,"left",0.2)
		time.sleep(5)
		restart = True
		return restart
	print("Entrando al menu amigos")
	time.sleep(12)
	coords_friend = imagesearch_loop(img_friend,0.01,0.9)
	click_image(img_friend,coords_friend,"left",0.2)
	print("Entrando al menu equipo")
	time.sleep(8)
	coords_start = imagesearch_loop(img_start,0.01,0.9)
	click_image(img_start,coords_start,"left",0.2)
	print("Tratando de skipear")
	time.sleep(25)
	coords_skip = imagesearch(img_skip)
	if coords_skip[0] != -1:
		click_image(img_skip,coords_skip,"left",0.2)
		print("Skip completado")
	else:
		print("Skip no encontrado")
	Is_A_Battle = avanzar()
	#control del avanzar
	x = True
	PH12 = True
	while x == True:
		if Is_A_Battle[1] == True:
			return
		while Is_A_Battle[0] == False:
			coords_baba = imagesearch(img_cancel)
			#Skip baba
			if coords_baba != -1:
				click_image(img_cancel,coords_baba,"left",0.2)
				Is_A_Battle = avanzar()
				break
			else:
				Is_A_Battle = avanzar()
				break
		while Is_A_Battle[0] == True:
			img_battle = "img/battle.png"
			if PH12 == True:
				coords_battle = imagesearch(img_battle,0.9)
				coords_orbe = [-1,-1]
				coords_orbe[0] = int(coords_battle[0])-170
				coords_orbe[1] = int(coords_battle[1])-220
				PH12 = False
			pyautogui.moveTo(coords_orbe[0], coords_orbe[1],0.5)
			print("Spam click")
			pyautogui.click(button="left")
			time.sleep(1)
			pyautogui.click(button="left")
			time.sleep(1)
			pyautogui.click(button="left")
			time.sleep(1)
			coords_1 = imagesearch(img_1,0.5)
			time.sleep(0.2)
			coords_2 = imagesearch(img_2,0.5)
			time.sleep(0.2)
			coords_3 = imagesearch(img_3,0.5)
			time.sleep(0.2)
			coords_4 = imagesearch(img_4,0.5)
			time.sleep(0.2)
			coords_5 = imagesearch(img_5,0.5)
			time.sleep(0.2)
			coords_6 = imagesearch(img_6,0.5)
			time.sleep(0.4)
			if coords_6[0] != -1:
				Is_A_Battle[0] = False
				print("Volviendo al mapa!")
				break
			elif coords_5[0] != -1:
				Is_A_Battle[0] = False
				print("Volviendo al mapa!")
				break
			elif coords_4[0] != -1:
				Is_A_Battle[0] = False
				print("Volviendo al mapa!")
				break
			elif coords_3[0] != -1:
				Is_A_Battle[0] = False
				print("Volviendo al mapa!")
				break
			elif coords_2[0] != -1:
				Is_A_Battle[0] = False
				print("Volviendo al mapa!")
				break
			elif coords_1[0] != -1:
				Is_A_Battle[0] = False
				print("Volviendo al mapa!")
				break
			
			
"""
attack()
ataca al enemigo
"""

def attack():
	img_battle = "img/battle.png"
	coords_battle = imagesearch(img_battle,0.9)
	coords_orbe = [-1,-1]
	coords_orbe[0] = int(coords_battle[0])-170
	coords_orbe[1] = int(coords_battle[1])-220
	pyautogui.moveTo(coords_orbe[0], coords_orbe[1],0.5)
	print("Ataque 1")
	pyautogui.click(button="left")
	time.sleep(4)
	print("Ataque 2")
	pyautogui.click(button="left")
	time.sleep(4)
	print("Ataque 3")
	pyautogui.click(button="left")
	print("Esperando 35 segundos")
	time.sleep(35)
	

	



"""
avanzar()
Elige el numero mas alto y clicka en el.
output:
Is_A_Battle = True si se encuentra en una batalla, False si no se encuentra en ella
"""
	
	
	
def avanzar():
	#Variables imagenes

	
	#Detectar si los numeros han salido ya
	Is_A_Battle = [False,False]
	x = True
	while x == True:
		coords_1 = imagesearch(img_1,0.5)
		time.sleep(0.2)
		coords_2 = imagesearch(img_2,0.5)
		time.sleep(0.2)
		coords_3 = imagesearch(img_3,0.5)
		time.sleep(0.2)
		coords_4 = imagesearch(img_4,0.5)
		time.sleep(0.2)
		coords_5 = imagesearch(img_5,0.5)
		time.sleep(0.2)
		coords_6 = imagesearch(img_6,0.5)
		time.sleep(0.4)
		coords_stone = imagesearch(img_stone)
		time.sleep(0.4)
		coords_lvl = imagesearch(img_lvl)
		if coords_lvl[0] != -1:
			print("¡Nivel finalizado con exito!")
			time.sleep(15)
			click_image(img_lvl,coords_lvl,"left",0.2)
			print("Se ha subido un nivel")
			time.sleep(6)
			coords_stone = imagesearch(img_stone)
			click_image(img_stone,coords_stone,"left",0.2)
			print("Recogiendo piedra.")
			time.sleep(5)
			coords_ok = imagesearch(img_ok)
			click_image(img_ok,coords_ok,"left",0.2)
			print("Saliendo de la pantalla de resumen.")
			time.sleep(5)
			coords_item = imagesearch(img_item)
			if coords_item[0] != -1:
				coords_ok = imagesearch(img_ok)
				click_image(img_ok,coords_ok,"left",0.2)
				time.sleep(5)
			coords_cancel = imagesearch(img_cancel)
			if coords_cancel != -1:
				click_image(img_cancel,coords_cancel,"left",0.2)
				print("Denegando amistad.")
				time.sleep(5)
			coords_home = imagesearch(img_home)
			click_image(img_home,coords_home,"left",0.2)
			print("Volviendo a la pantalla de inicio.")
			Is_A_Battle[1] = True
			return Is_A_Battle
		if coords_stone[0] != -1:
			print("¡Nivel finalizado con exito!")
			time.sleep(15)
			click_image(img_stone,coords_stone,"left",0.2)
			print("Recogiendo piedra.")
			time.sleep(5)
			coords_ok = imagesearch(img_ok)
			click_image(img_ok,coords_ok,"left",0.2)
			print("Saliendo de la pantalla de resumen.")
			time.sleep(5)
			coords_item = imagesearch(img_item)
			if coords_item[0] != -1:
				coords_ok = imagesearch(img_ok)
				click_image(img_ok,coords_ok,"left",0.2)
				time.sleep(5)
			coords_cancel = imagesearch(img_cancel)
			if coords_cancel != -1:
				click_image(img_cancel,coords_cancel,"left",0.2)
				print("Denegando amistad.")
				time.sleep(5)
			coords_home = imagesearch(img_home)
			click_image(img_home,coords_home,"left",0.2)
			print("Volviendo a la pantalla de inicio.")
			Is_A_Battle[1] = True
			return Is_A_Battle
		coords_skip = imagesearch(img_skip)
		if coords_skip[0] != -1:
			click_image(img_skip,coords_skip,"left",0.2)
			time.sleep(15)
			print("¡Nivel con skip finalizado con exito!")
			coords_lvl = imagesearch(img_lvl)
			if coords_lvl != -1:
				click_image(img_lvl,coords_lvl,"left",0.2)
				print("Se ha subido un nivel")
				time.sleep(6)
			coords_stone = imagesearch(img_stone)
			click_image(img_stone,coords_stone,"left",0.2)
			print("Recogiendo piedra.")
			coords_ok = imagesearch(img_ok)
			click_image(img_ok,coords_ok,"left",0.2)
			print("Saliendo de la pantalla de resumen.")
			time.sleep(5)
			coords_item = imagesearch(img_item)
			if coords_item[0] != -1:
				coords_ok = imagesearch(img_ok)
				click_image(img_ok,coords_ok,"left",0.2)
				time.sleep(5)
			coords_cancel = imagesearch(img_cancel)
			if coords_cancel != -1:
				click_image(img_cancel,coords_cancel,"left",0.2)
				print("Denegando amistad.")
				time.sleep(5)
			coords_home = imagesearch(img_home)
			click_image(img_ok,coords_ok,"left",0.2)
			print("Volviendo a la pantalla de inicio.")
			Is_A_Battle[1] = True
			return Is_A_Battle
		
		
		if coords_6[0] != -1:
			break
		elif coords_5[0] != -1:
			break
		elif coords_4[0] != -1:
			break
		elif coords_3[0] != -1:
			break
		elif coords_2[0] != -1:
			break
		elif coords_1[0] != -1:
			break
		print("Buscando numeros, nada encontrado.")
	
	
	while x == True:
		coords_1 = imagesearch(img_1,0.5)
		time.sleep(0.2)
		coords_2 = imagesearch(img_2,0.5)
		time.sleep(0.2)
		coords_3 = imagesearch(img_3,0.5)
		time.sleep(0.2)
		coords_4 = imagesearch(img_4,0.5)
		time.sleep(0.2)
		coords_5 = imagesearch(img_5,0.5)
		time.sleep(0.2)
		coords_6 = imagesearch(img_6,0.5)
		time.sleep(0.5)
		
		if coords_6[0] != -1:
			coords_click_num = coords_6
			wait = 6
			break
		elif coords_5[0] != -1:
			coords_click_num = coords_5
			wait = 5
			break
		elif coords_4[0] != -1:
			coords_click_num = coords_4
			wait = 4
			break
		elif coords_3[0] != -1:
			coords_click_num = coords_3
			wait = 3
			break
		elif coords_2[0] != -1:
			coords_click_num = coords_2
			wait = 2
			break
		elif coords_1[0] != -1:
			coords_click_num = coords_1
			wait = 1
			break
	print("Click en "+str(wait)+".")
	click_image(img_1,coords_click_num,"left",0.5)
	print("Esperando "+str(3+wait)+" segundos.")
	time.sleep(3+wait)
	#modulo direccion
	coords_up = imagesearch_loop_skip(img_up,1)
	time.sleep(0.2)
	coords_down = imagesearch_loop_skip(img_down,1)
	time.sleep(0.2)
	coords_right = imagesearch_loop_skip(img_right,1)
	time.sleep(0.2)
	coords_left = imagesearch_loop_skip(img_left,1)
	time.sleep(0.2)
	
	if coords_up[0] != -1:
		click_image(img_up,coords_up,"left",0.5,0.9)
		print("Esperando "+str(10+wait)+" segundos.")
		time.sleep(wait+10)
	elif coords_down[0] != -1:
		click_image(img_down,coords_down,"left",0.5,0.9)
		print("Esperando "+str(10+wait)+" segundos.")
		time.sleep(wait+10)
	elif coords_left[0] != -1:
		click_image(img_left,coords_left,"left",0.5,0.9)
		print("Esperando "+str(10+wait)+" segundos.")
		time.sleep(wait+10)
	elif coords_right[0] != -1:
		click_image(img_right,coords_right,"left",0.5,0.9)
		print("Esperando "+str(10+wait)+" segundos.")
		time.sleep(wait+10)
		
	time.sleep(5)
	Battle = imagesearch(img_battle,0.9)
	if Battle[0] != -1:
		Is_A_Battle[0] = True
	else:
		Is_A_Battle[0] = False
	return Is_A_Battle
	
	
	
	
"""
imagesearch_loop_skip()
imputs:
image = ruta de la imagenes
skipafter = Segundos hasta abortar la busqueda.
precision = precision de la busqueda
outupt:
posicion de la imagen. si no encuentra nada, [-1,-1]
"""
	
def imagesearch_loop_skip(image,skipafter=1,precision=0.8):
	pos = imagesearch(image, precision)
	count = 0
	while pos[0] == -1:
		print(image+" not found, waiting")
		time.sleep(0.1)
		if count >= skipafter*5:
			pos = imagesearch(image, precision)
			print(image+" not found after "+str(skipafter)+" seconds, skipping.")
			break
		else:
			count = count+1
		pos = imagesearch(image, precision)
	print("Imagen "+str(image)+" encontrada en "+str(pos)+".")
	return pos
	
	
	
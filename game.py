import random
import os
import time
import sys

class chat:
	def __init__(self,duree,sexe,position,apparence):
		self.duree = duree
		self.sexe = sexe
		self.position = position
		self.apparence =apparence
		
class souris:
	def __init__(self,duree,sexe,position,apparence):
		self.duree = duree
		self.sexe = sexe
		self.position = position
		self.apparence = apparence

class graine:
	def __init__(self,position,apparence):
		self.position = position
		self.apparence = apparence


		
#Les Objets
chat_c  = [	chat(150,"M",random.randint(259,259),"¤"),
			chat(150,"M",random.randint(19, 29),"¤"),
			chat(150,"M",random.randint(209,230),"¤"),
			chat(150,"M",random.randint(300,309),"¤"),
			chat(150,"M",random.randint(100, 208),"¤")];
souris_s  = [souris(500,"M",random.randint(227, 227),"~"),
			souris(500,"M",random.randint(190, 209),"~"),
			souris(500,"M",random.randint(20, 299),"~"),
			souris(500,"M",random.randint(59,300),"~"),
			souris(500,"M",random.randint(100, 208),"~")];

graine_g = [graine(random.randint(1, 100),"."),
			graine(random.randint(100, 150),"."),
			graine(random.randint(150, 250),"."),
			graine(random.randint(300,350),"."),
			graine(random.randint(350, 380),".")];




nbre_ligne = 20
nbre_colonne = 20
n = nbre_ligne * nbre_colonne
zone = [' ']*n	
zone_off = ['_']*33
zone_card = ['_']*20

i=0
j=79
while j <=399:
	zone[j] = "<|\n"
	j+=80


k=0
while k <=320:
	zone[k] = "|>"
	k+=80


#(¤v¤) <:o>~
cpt_chat=5
cpt_souris=5
i+=0
while i<n*3:
	time.sleep(0.01)
	os.system("cls")
	print("\t \t\t \t-CAT AND MOUSE- :)")
	sys.stdout.write(f"\t \t\t \t_____(. .)_____")
	sys.stdout.write(f"\n\t \t\t \t      v v      ")
	print('\n\n')
	sys.stdout.write(f"|")
	for objet in zone_card:
		sys.stdout.write(f"^^^")
		sys.stdout.write(f"^")
	sys.stdout.write(f"|")

	k=0
	while k <=320:
		zone[k] = "\n|>"
		k+=80
	
	x=0
	y=0
	while x<5:
		while y<5:
			if chat_c[x].position == souris_s[y].position  and souris_s[y].position!=399 and souris_s[y].apparence != ' ' and chat_c[x].apparence!=' ':
				souris_s[y].apparence = ' '
				souris_s[y].position =399
				souris_s[y].duree=0
				if chat_c[x].position<399 and chat_c[x].duree!=0:
					chat_c[x].duree+=100
				else :
					chat_c[x].duree=00

			y+=1
		x+=1


	x=0
	y=0
	while x<5:
		while y<5:
			if souris_s[x].position == graine_g[y].position  and graine_g[y].position!=399 and graine_g[y].apparence != ' ':
				graine_g[y].apparence = ' '
				graine_g[y].position =399
				if souris_s[x].position<399 and souris_s[x].duree!=0 and souris_s[x].apparence!=' ':
					souris_s[x].duree+=100
				else :
					souris_s[x].duree=00

			y+=1
		x+=1

	if graine_g[0].position == souris_s[0].position:
		graine_g[0].apparence = ' '
		souris_s[0].duree +=1 


	#Utlisation des objets.
	c=0
	while c<5:
		zone[chat_c[c].position] = chat_c[c].apparence
		zone[souris_s[c].position] = souris_s[c].apparence
		zone[graine_g[c].position] = graine_g[c].apparence
		c+=1

	


	#Afichage de notre zone de jeu
	for objet in zone:
		k=0
		while k <=320:
			zone[k] = "|>"
			k+=80

		sys.stdout.write(f"{objet}")

		j=79
		while j <=399:
			zone[j] = "<|\n"
			j+=80
	
		#Sortie
		if(i==400 and cpt_chat != 0 or cpt_souris !=0):
			i=0
		if(cpt_chat == 0 and cpt_souris ==0):
			zone[198] = "E"
			zone[202] = "N"
			zone[206] = "D"
			i == 800
		i+=1


	c=0
	while c<5:
		if chat_c[c].position == 399 or chat_c[c].position == 79 or chat_c[c].position == 159 or chat_c[c].position == 240 or chat_c[c].position == 319 and chat_c[c].duree!=0:
			chat_c[c].position = random.randint(1, 390)
		if chat_c[c].position == 0 or chat_c[c].position == 80 or chat_c[c].position == 160 or chat_c[c].position == 240 or chat_c[c].position == 320 and chat_c[c].duree!=0 :
			zone[chat_c[c].position] = " "
			chat_c[c].position = random.randint(1, 390)
		else:
			zone[chat_c[c].position] = ' '
		if souris_s[c].position == 399 or souris_s[c].position == 79 or souris_s[c].position == 159 or souris_s[c].position == 240 or souris_s[c].position == 319 and souris_s[c].duree!=0 :
			zone[souris_s[c].position] = " "
			souris_s[c].position = random.randint(5, 390)
		if souris_s[c].position == 0 or souris_s[c].position == 80 or souris_s[c].position == 160 or souris_s[c].position == 240 or souris_s[c].position == 320 and souris_s[c].duree!=0 :
			zone[souris_s[c].position] = " "
			souris_s[c].position = random.randint(5, 390)
		else:
			zone[souris_s[c].position] = ' '
	
		if chat_c[c].duree ==0:
			chat_c[c].apparence = ' '
		if souris_s[c].duree ==0:
			souris_s[c].apparence=' '


		x=c
		y=0
		while x<5:
			while y<5:
				if chat_c[x].position == souris_s[y].position  and souris_s[y].position!=399 and souris_s[y].apparence != ' ' and chat_c[x].apparence!=' ':
					souris_s[y].apparence = ' '
					souris_s[y].position =399
					souris_s[y].duree=0
					if chat_c[x].position<=399 and chat_c[x].duree!=0:
						chat_c[x].duree+=100
					else :
						chat_c[x].duree=00
					
				y+=1
			x+=1

		x=c
		y=0
		while x<5:
			while y<5:
				if souris_s[x].position == graine_g[y].position  and graine_g[y].position!=399 and graine_g[y].apparence != ' ':
					graine_g[y].apparence = ' '
					graine_g[y].position =399
					if souris_s[x].position<399 and souris_s[x].duree!=0 and souris_s[x].apparence!=' ':
						souris_s[x].duree+=100
					else :
						souris_s[x].duree=00
	
				y+=1
			x+=1


	
		if chat_c[c].apparence !=' ':
			chat_c[c].position+=random.randint(-0, 1)
			if chat_c[c].duree>0:
				chat_c[c].duree-=1
			else:
				chat_c[c].apparence = ' '
				chat_c[c].position=398
				chat_c[c].sexe="M"

		if chat_c[c].duree ==0:
			chat_c[c].apparence = ' '
		if souris_s[c].duree ==0:
			souris_s[c].apparence=' '


		x=c
		y=0
		while x<5:
			while y<5:
				if chat_c[x].position == souris_s[y].position  and souris_s[y].position!=399 and souris_s[y].apparence != ' ' and chat_c[x].apparence!=' ':
					souris_s[y].apparence = ' '
					souris_s[y].position =399
					souris_s[y].duree=0
					if chat_c[x].position<399 and chat_c[x].duree!=0:
						chat_c[x].duree+=100
					else :
						chat_c[x].duree=00

					
				y+=1
			x+=1

		x=c
		y=0
		while x<5:
			while y<5:
				if souris_s[x].position == graine_g[y].position  and graine_g[y].position!=399 and graine_g[y].apparence != ' ':
					graine_g[y].apparence = ' '
					graine_g[y].position =399
					if souris_s[x].position<399 and souris_s[x].duree!=0 and souris_s[x].apparence!=' ':
						souris_s[x].duree+=100
					else :
						souris_s[x].duree=00
	
				y+=1
			x+=1


		if souris_s[c].apparence !=' ':
			souris_s[c].position-=random.randint(0, 1)
			if souris_s[c].duree>0:
				souris_s[c].duree-=1
			else:
				souris_s[c].apparence = ' '
				souris_s[c].position=399
				souris_s[c].sexe="M"
		x=c
		y=0
		while x<5:
			while y<5:
				if chat_c[x].position == souris_s[y].position  and souris_s[y].position!=399 and souris_s[y].apparence != ' ' and chat_c[x].apparence!=' ':
					souris_s[y].apparence = ' '
					souris_s[y].position=399
					souris_s[y].duree=0
					if chat_c[x].position<399 and chat_c[x].duree!=0:
						chat_c[x].duree+=100
					else :
						chat_c[x].duree=00
					
				y+=1
			x+=1
		

	
		
		if chat_c[c].position > 380 or chat_c[c].position == 78 or chat_c[c].position == 157 or chat_c[c].position == 158 or chat_c[c].position == 159  or chat_c[c].position == 238 or chat_c[c].position == 318 or chat_c[c].position == 0 or chat_c[c].position == 80 or chat_c[c].position == 160 or chat_c[c].position == 240 or chat_c[c].position == 320:
			if chat_c[c].duree<=0:
				chat_c[c].duree=0
				chat_c[c].apparence = ' '
				chat_c[c].position=399
				chat_c[c].sexe="M"
			else:
				chat_c[c].duree-=1
				chat_c[c].position=random.randint(1, 350)
			
		if souris_s[c].position > 380 or souris_s[c].position == 78 or souris_s[c].position == 157 or souris_s[c].position == 158 or souris_s[c].position == 159  or souris_s[c].position == 238 or souris_s[c].position == 318 or souris_s[c].position == 0 or souris_s[c].position == 80 or souris_s[c].position == 160 or souris_s[c].position == 240 or souris_s[c].position == 320:
			if souris_s[c].duree<=0:
				souris_s[c].duree=0
				souris_s[c].apparence = ' '
				souris_s[c].position=399
				souris_s[c].sexe="M"
			else:
				souris_s[c].duree-=1
				souris_s[c].position=random.randint(1, 350)
	
	
		c+=1

	j=79
	while j <=399:
		zone[j] = "<|\n"
		j+=80
	sys.stdout.write(f"|")
	for objet in zone_card:
		sys.stdout.write(f"vvv")
		sys.stdout.write(f"v")
	sys.stdout.write(f"|")


	


#Statistique 
	print('\n \tChat -> (¤) \t Souris -> (~) \tGraine -> (.)')
	for objet in zone_off*2:
		sys.stdout.write(f"{objet}")
	print('\n>\t\t\t\t\t\t\t\t <')
	sys.stdout.write(f">  \t\t\t  Duree de vie \t\t\t\t <\n")

	for objet in zone_off*2:
		sys.stdout.write(f"{objet}")
	val = 0
	cpt_chat=5
	cpt_souris=5
	cpt_graine = 5
	while val<5:
		sys.stdout.write(f"\n> \tChat {val+1}:{chat_c[val].duree} \t\t|\t\t Souris {val+1}:{souris_s[val].duree} \t <")
		if chat_c[val].duree ==0:
			cpt_chat-=1
		if souris_s[val].duree ==0:
			cpt_souris-=1
		if cpt_graine !=0:	
			if graine_g[val].apparence ==' ':
				cpt_graine-=1
		if(cpt_chat == 0 and cpt_souris ==0):
			i == 400
		val+=1
	print('')
	for objet in zone_off*2:
		sys.stdout.write(f"^")

	sys.stdout.write(f"\n>\tChat :{cpt_chat} \tSouris:{cpt_souris} \tGraine:{cpt_graine} \t\t <")
	

	print('')
	for objet in zone_off*2:
		sys.stdout.write(f"^")
	print('\n')

# Kamen Rider - (C)1971-2021 Toei Company and Ishimori Pro.

import time,random as r
import krs_string as kstring,krs_Rider as rider,krs_kaijin as kaijin

rt=("KR1","KR2","V3","AMZ","BLK","RX")
kj=("DMK","MMC","HHP","MMK","FFG","JJL","SSK","CCP","HHG","PTB","CBM","ESN","CKN","SPC")
level={
	0:{
		"kaijin":[kj[r.randrange(9,14)] for i in range(2)]
	},
	1:{
		"kaijin":[kj[r.randrange(1,9)] for i in range(3)]
	},
	2:{
		"kaijin":[kj[0]]
	},
}
riderStats={
	"hp":50000,
	"atk":0,
	"def":0,
	"spd":0,
	"crit":0.0
}
kaijinStats={
	"hp":0,
	"atk":0,
	"def":0,
	"spd":0,
	"crit":0.0
}
gameOver=False
kaijinKilled=False

def printphoto(n):
	for i in kstring.photo[n]:
		print(i)

def printlevel(lv):
	kstring.level[20]=kstring.kaijin[kj.index(level[0]["kaijin"][0])]
	kstring.level[22]=kstring.kaijin[kj.index(level[0]["kaijin"][1])]
	kstring.level[9]=kstring.kaijin[kj.index(level[1]["kaijin"][0])]
	kstring.level[11]=kstring.kaijin[kj.index(level[1]["kaijin"][1])]
	kstring.level[13]=kstring.kaijin[kj.index(level[1]["kaijin"][2])]
	if int(lv)==0:
		for i in kstring.level:
			print(i)
	elif int(lv)==1:
		for i in range(16):
			print(kstring.level[i])
	elif int(lv)==2:
		for i in range(5):
			print(kstring.level[i])

for i in kstring.spmsg:
	print(i)
input("\n"*2+"PRESS ENTER TO CONTINUE.")
print("\n"*50)
while True:
	print("\n"*50)
	printphoto(0)
	print("======------ Kamen Rider Showdown ------======\n\n   PROGRAMMED BY Katsumi Kogen ~ Python 3.8\n")
	print("                < 1 > --- PLAY\n\n                < 2 > --- QUIT")
	menuSelect=input("                      ")
	if menuSelect=="2":
		time.sleep(1)
		break
	elif menuSelect=="1":
	
		#main function
		while True:
			for i in kstring.menu:
				print(i)
			riderSelection=input()
			if riderSelection not in [str(i) for i in range(1,7)]:
				print("INVALID INPUT!")
				time.sleep(1)
			else:
				pRider=int(riderSelection)-1
				kstring.select[4]=kstring.selected[pRider]
				break
		for i in kstring.select:
			print(i)
		input()
		printphoto(pRider)
		print("Wait here for a moment...")
		time.sleep(r.uniform(1,10.001))
		
		print("----- INFORMATION -----\nYour Rider: "+
		rider.rider[rt[pRider]]["title"]+
		"\nName: "+rider.rider[rt[pRider]]["name"]+"\n")
		time.sleep(2)
		for i in rider.rider[rt[pRider]]["desc"]:
			print(i)
			time.sleep(0.02)
		time.sleep(2)
		print("\nATK: "+str(rider.rider[rt[pRider]]["atk"])+
		"\nDEF: "+str(rider.rider[rt[pRider]]["def"])+
		"\nSPD: "+str(rider.rider[rt[pRider]]["spd"]))
		input("\nPress ENTER to confirm.\n")
		
		#level 1
		printlevel(0)
		time.sleep(2)
		dmg=lambda val1,val2:(val1+val2)*(3/2)
		for i in level[0]["kaijin"]:
			print(rider.rider[rt[pRider]]["title"]+" VS. "+kaijin.kaijin[i]["name"])
			for j in ("atk","def","spd","crit"):
				riderStats[j]=rider.rider[rt[pRider]][j]
			for j in kaijinStats:
				kaijinStats[j]=kaijin.kaijin[i][j]
			input("----- KAMEN RIDER SHOWDOWN -----\n\n    Are you ready for battle?\n\n----- KAMEN RIDER SHOWDOWN -----")
			powGauge,max=0,10000
			
			while True:
				print(rider.rider[rt[pRider]]["title"]+" ["+
				str(riderStats["hp"])+"]\n"+
				kaijin.kaijin[i]["name"]+" ["+str(kaijinStats["hp"])+"]")
				time.sleep(0.1)
				print("RIDER'S TURN (1-4)")
				for move in rider.rider[rt[pRider]]["move"]["name"]:
					print("< "+move+" >")
				while True:
					cmd=input()
					if cmd not in "1234":
						print("Invalid input!")
					else:
						break
				print(rider.rider[rt[pRider]]["title"]+" uses "+
				rider.rider[rt[pRider]]["move"]["name"][int(cmd)-1]+"!")
				evade=(True,False)[r.randrange(2)]
				if evade:
					print(kaijin.kaijin[i]["name"]+" evades!")
				else:
					dval=int(dmg(r.randrange(1,100),rider.rider[rt[pRider]]["move"]["dmg"][int(cmd)-1])*(riderStats["atk"]*0.1)+riderStats["spd"]/2-kaijinStats["def"]*0.6)
					if powGauge>=max:
						dval+=int(powGauge*(4/5)*riderStats["crit"]*1/2)
						print("Critical damage!")
						time.sleep(0.05)
						powGauge=0
					kaijinStats["hp"]-=dval
					print(kaijin.kaijin[i]["name"]+" -"+str(dval)+" HP")
				time.sleep(1)
				print("KAIJIN'S TURN")
				evade=(True,False)[r.randrange(2)]
				if evade:
					print(rider.rider[rt[pRider]]["title"]+" evades!")
				else:
					dval=int(dmg(r.randrange(1,100),30*(kaijinStats["atk"]*0.1)+kaijinStats["spd"]/2-riderStats["def"]*0.6))
					riderStats["hp"]-=dval
					powGauge+=dval
					print(rider.rider[rt[pRider]]["title"]+" -"+str(dval)+" HP")
					time.sleep(1)
				if riderStats["hp"]<=0:
					break
				elif kaijinStats["hp"]<=0:
					break
			if riderStats["hp"]<=0:
				input("-----===== GAME OVER =====-----\nPress ENTER to exit the program")
				sys.exit()
			elif kaijinStats["hp"]<=0:
				print("Rider Kick!!!")
				time.sleep(1)
				riderStats["hp"]*=2
				for j in ("hp","atk","def","spd","crit"):
					riderStats[j]*=1.25
				input(kaijin.kaijin[i]["name"]+" is destroyed!\nThank you, "+rider.rider[rt[pRider]]["title"]+"!")
		
		#level 2
		printlevel(1)
		time.sleep(2)
		dmg=lambda val1,val2:(val1+val2)*(8/7)
		for i in level[1]["kaijin"]:
			print(rider.rider[rt[pRider]]["title"]+" VS. "+kaijin.kaijin[i]["name"])
			for j in ("atk","def","spd","crit"):
				riderStats[j]=rider.rider[rt[pRider]][j]
			for j in kaijinStats:
				kaijinStats[j]=kaijin.kaijin[i][j]
			input("----- KAMEN RIDER SHOWDOWN -----\n\n    Are you ready for battle?\n\n----- KAMEN RIDER SHOWDOWN -----")
			powGauge,max=0,20000
			
			while True:
				print(rider.rider[rt[pRider]]["title"]+" ["+
				str(riderStats["hp"])+"]\n"+
				kaijin.kaijin[i]["name"]+" ["+str(kaijinStats["hp"])+"]")
				time.sleep(0.1)
				print("RIDER'S TURN (1-4)")
				for move in rider.rider[rt[pRider]]["move"]["name"]:
					print("< "+move+" >")
				while True:
					cmd=input()
					if cmd not in "1234":
						print("Invalid input!")
					else:
						break
				print(rider.rider[rt[pRider]]["title"]+" uses "+
				rider.rider[rt[pRider]]["move"]["name"][int(cmd)-1]+"!")
				evade=(True,False)[r.randrange(2)]
				if evade:
					print(kaijin.kaijin[i]["name"]+" evades!")
				else:
					dval=int(dmg(r.randrange(1,100),rider.rider[rt[pRider]]["move"]["dmg"][int(cmd)-1])*(riderStats["atk"]*0.1)+riderStats["spd"]/2-kaijinStats["def"]*0.6)
					if powGauge>=max:
						dval+=int(powGauge*(4/5)*riderStats["crit"]*1/2)
						print("Critical damage!")
						time.sleep(0.05)
						powGauge=0
					kaijinStats["hp"]-=dval
					print(kaijin.kaijin[i]["name"]+" -"+str(dval)+" HP")
				time.sleep(1)
				print("KAIJIN'S TURN")
				evade=(True,False)[r.randrange(2)]
				if evade:
					print(rider.rider[rt[pRider]]["title"]+" evades!")
				else:
					dval=int(dmg(r.randrange(1,100),30*(kaijinStats["atk"]*0.1)+kaijinStats["spd"]/2-riderStats["def"]*0.6))
					riderStats["hp"]-=dval
					powGauge+=dval
					print(rider.rider[rt[pRider]]["title"]+" -"+str(dval)+" HP")
					time.sleep(1)
				if riderStats["hp"]<=0:
					break
				elif kaijinStats["hp"]<=0:
					break
			if riderStats["hp"]<=0:
				input("-----===== GAME OVER =====-----\nPress ENTER to exit the program")
				sys.exit()
			elif kaijinStats["hp"]<=0:
				print("Rider Kick!!!")
				time.sleep(1)
				riderStats["hp"]*=2
				for j in ("hp","atk","def","spd","crit"):
					riderStats[j]*=1.25
				input(kaijin.kaijin[i]["name"]+" is destroyed!\nThank you, "+rider.rider[rt[pRider]]["title"]+"!")
		
		#level 3
		printlevel(2)
		time.sleep(2)
		dmg=lambda val1,val2:(val1+val2)*(10/9)
		for i in level[2]["kaijin"]:
			print(rider.rider[rt[pRider]]["title"]+" VS. "+kaijin.kaijin[i]["name"])
			for j in ("atk","def","spd","crit"):
				riderStats[j]=rider.rider[rt[pRider]][j]
			for j in kaijinStats:
				kaijinStats[j]=kaijin.kaijin[i][j]
			input("----- KAMEN RIDER SHOWDOWN -----\n\n    Are you ready for battle?\n\n----- KAMEN RIDER SHOWDOWN -----")
			powGauge,max=0,20000
			
			while True:
				print(rider.rider[rt[pRider]]["title"]+" ["+
				str(riderStats["hp"])+"]\n"+
				kaijin.kaijin[i]["name"]+" ["+str(kaijinStats["hp"])+"]")
				time.sleep(0.1)
				print("RIDER'S TURN (1-4)")
				for move in rider.rider[rt[pRider]]["move"]["name"]:
					print("< "+move+" >")
				while True:
					cmd=input()
					if cmd not in "1234":
						print("Invalid input!")
					else:
						break
				print(rider.rider[rt[pRider]]["title"]+" uses "+
				rider.rider[rt[pRider]]["move"]["name"][int(cmd)-1]+"!")
				evade=(True,False)[r.randrange(2)]
				if evade:
					print(kaijin.kaijin[i]["name"]+" evades!")
				else:
					dval=int(dmg(r.randrange(1,100),rider.rider[rt[pRider]]["move"]["dmg"][int(cmd)-1])*(riderStats["atk"]*0.1)+riderStats["spd"]/2-kaijinStats["def"]*0.6)
					if powGauge>=max:
						dval+=int(powGauge*(4/5)*riderStats["crit"]*1/2)
						print("Critical damage!")
						time.sleep(0.05)
						powGauge=0
					kaijinStats["hp"]-=dval
					print(kaijin.kaijin[i]["name"]+" -"+str(dval)+" HP")
				time.sleep(1)
				print("KAIJIN'S TURN")
				evade=(True,False)[r.randrange(2)]
				if evade:
					print(rider.rider[rt[pRider]]["title"]+" evades!")
				else:
					dval=int(dmg(r.randrange(1,100),30*(kaijinStats["atk"]*0.1)+kaijinStats["spd"]/2-riderStats["def"]*0.6))
					riderStats["hp"]-=dval
					powGauge+=dval
					print(rider.rider[rt[pRider]]["title"]+" -"+str(dval)+" HP")
					time.sleep(1)
				if riderStats["hp"]<=0:
					break
				elif kaijinStats["hp"]<=0:
					break
			if riderStats["hp"]<=0:
				input("-----===== GAME OVER =====-----\nPress ENTER to exit the program")
				sys.exit()
			elif kaijinStats["hp"]<=0:
				print("Rider Kick!!!")
				time.sleep(1)
				input(kaijin.kaijin[i]["name"]+" is destroyed!\nThank you, "+rider.rider[rt[pRider]]["title"]+"!")
import tkinter as tk
from tkinter import *
from tkinter import ttk
import random
from time import sleep


rating_T1 = 0
rating_T2 = 0
rozdil = 0
ratingy =[0,0]
kdo_vyhral = []
silnejsi_tym = 0
vysledek = ""
vitez = ""
vysledky_1 = ["1:0", "1:0", "1:0", "2:0", "2:0", "2:1", "2:1", "2:1", "3:1", "3:2", "3:2", "4:3", "5:4", "5:3", "6:4", "6:5"]
vysledky_2 = ["1:0", "3:1", "3:1", "3:1", "4:1", "2:0", "2:0", "2:0", "3:0", "4:1", "4:2", "4:2", "5:2", "5:4", "5:3", "6:3", "7:4", ]
vysledky_3 = ["3:0", "3:0", "6:3", "3:0", "7:4", "4:0", "4:0", "4:0", "7:4", "3:0", "3:1", "2:0", "5:0", "5:1", "7:2", "5:1", "4:1", "7:2", "4:1", "6:0", "6:1", "6:1", "6:2", "6:2", "6:2", "6:3", "6:3"]
vysledky_4 = ["12:0", "11:1", "10:0", "7:0", "8:0", "9:0", "7:0", "7:0", "8:0", "8:0", "7:0", "5:0", "6:0", "6:0", "5:0", "8:1", "8:1", "9:1", "9:1"]
pocet_vyher_tym_1 = 0
pocet_vyher_tym_2 = 0

window = tk.Tk()

#window.geometry("700x1600")

def zadani_tymu_1():
   zadavani_T1.tkraise()

def zadani_tymu_2():
   zadavani_T2.tkraise()

def ukaz_uvodni_stranu_tym_1():
	rating_T1 = 0
	if var_chck_T1_1.get() == 1:
		rating_T1 += int(entry_T1_1.get())
	else:
		rating_T1 += int(entry_T1_1.get())*0.8

	if var_chck_T1_2.get() == 1:
		rating_T1 += int(entry_T1_2.get())
	else:
		rating_T1 += int(entry_T1_2.get())*0.8

	if var_chck_T1_3.get() == 1:
		rating_T1 += int(entry_T1_3.get())
	else:
		rating_T1 += int(entry_T1_3.get())*0.8

	if var_chck_T1_4.get() == 1:
		rating_T1 += int(entry_T1_4.get())
	else:
		rating_T1 += int(entry_T1_4.get())*0.8

	if var_chck_T1_5.get() == 1:
		rating_T1 += int(entry_T1_5.get())
	else:
		rating_T1 += int(entry_T1_5.get())*0.8

	if var_chck_T1_6.get() == 1:
		rating_T1 += int(entry_T1_6.get())
	else:
		rating_T1 += int(entry_T1_6.get())*0.8

	if var_chck_T1_7.get() == 1:
		rating_T1 += int(entry_T1_7.get())
	else:
		rating_T1 += int(entry_T1_7.get())*0.8

	if var_chck_T1_8.get() == 1:
		rating_T1 += int(entry_T1_8.get())
	else:
		rating_T1 += int(entry_T1_8.get())*0.8

	if var_chck_T1_9.get() == 1:
		rating_T1 += int(entry_T1_9.get())
	else:
		rating_T1 += int(entry_T1_9.get())*0.8

	if var_chck_T1_10.get() == 1:
		rating_T1 += int(entry_T1_10.get())
	else:
		rating_T1 += int(entry_T1_10.get())*0.8

	if var_chck_T1_11.get() == 1:
		rating_T1 += int(entry_T1_11.get())
	else:
		rating_T1 += int(entry_T1_11.get())*0.8

	label_rating_T1 .config(text="Rating týmu 1: " + str(rating_T1))
	ratingy[0]= rating_T1
	rozdil = abs(ratingy[0]-ratingy[1])
	label_rozdil.config( text="Rozdíl: " + str(rozdil))
	uvodni_strana.tkraise()


def ukaz_uvodni_stranu_tym_2():
	rating_T2 = 0
	if var_chck_T2_1.get() == 1:
		rating_T2 += int(entry_T2_1.get())
	else:
		rating_T2 += int(entry_T2_1.get())*0.8

	if var_chck_T2_2.get() == 1:
		rating_T2 += int(entry_T2_2.get())
	else:
		rating_T2 += int(entry_T2_2.get())*0.8

	if var_chck_T2_3.get() == 1:
		rating_T2 += int(entry_T2_3.get())
	else:
		rating_T2 += int(entry_T2_3.get())*0.8

	if var_chck_T2_4.get() == 1:
		rating_T2 += int(entry_T2_4.get())
	else:
		rating_T2 += int(entry_T2_4.get())*0.8

	if var_chck_T2_5.get() == 1:
		rating_T2 += int(entry_T2_5.get())
	else:
		rating_T2 += int(entry_T2_5.get())*0.8

	if var_chck_T2_6.get() == 1:
		rating_T2 += int(entry_T2_6.get())
	else:
		rating_T2 += int(entry_T2_6.get())*0.8

	if var_chck_T2_7.get() == 1:
		rating_T2 += int(entry_T2_7.get())
	else:
		rating_T2 += int(entry_T2_7.get())*0.8

	if var_chck_T2_8.get() == 1:
		rating_T2 += int(entry_T2_8.get())
	else:
		rating_T2 += int(entry_T2_8.get())*0.8

	if var_chck_T2_9.get() == 1:
		rating_T2 += int(entry_T2_9.get())
	else:
		rating_T2 += int(entry_T2_9.get())*0.8

	if var_chck_T2_10.get() == 1:
		rating_T2 += int(entry_T2_10.get())
	else:
		rating_T2 += int(entry_T2_10.get())*0.8

	if var_chck_T2_11.get() == 1:
		rating_T2 += int(entry_T2_11.get())
	else:
		rating_T2 += int(entry_T2_11.get())*0.8

	label_rating_T2 .config(text="Rating týmu 2: " + str(rating_T2))

	ratingy[1]= rating_T2
	rozdil = abs(ratingy[0]-ratingy[1])
	label_rozdil.config( text="Rozdíl: " + str(rozdil))
	uvodni_strana.tkraise()



def ukaz_uvodni_stranu_start():
	uvodni_strana.tkraise()

def vygeneruj_vysledek():
	print(ratingy)
	tym_1 = ratingy[0]
	tym_2 = ratingy[1]
	rozdil_ratingu = abs(ratingy[0]-ratingy[1])
	pocet_vyher_tym_1 = 0
	pocet_vyher_tym_2 = 0
	if tym_1 > tym_2:
		silnejsi_tym = 1
		print(f"\nTým 1 je silnější a rozdíl ratingů je {rozdil_ratingu}")
	
		if rozdil_ratingu <= 22:
			for i in range(50):
				kdo_vyhral.append("tym_1")
			for i in range(50):
				kdo_vyhral.append("tym_2")
		elif rozdil_ratingu <= 33:
			for i in range(55):
				kdo_vyhral.append("tym_1")
			for i in range(45):
				kdo_vyhral.append("tym_2")
		elif rozdil_ratingu <= 44:
			for i in range(60):
				kdo_vyhral.append("tym_1")
			for i in range(40):
				kdo_vyhral.append("tym_2")
		elif rozdil_ratingu <= 66:
			for i in range(65):
				kdo_vyhral.append("tym_1")
			for i in range(35):
				kdo_vyhral.append("tym_2")
		elif rozdil_ratingu <= 88:
			for i in range(70):
				kdo_vyhral.append("tym_1")
			for i in range(30):
				kdo_vyhral.append("tym_2")
		elif rozdil_ratingu <= 121:
			for i in range(75):
				kdo_vyhral.append("tym_1")
			for i in range(25):
				kdo_vyhral.append("tym_2")
		elif rozdil_ratingu <= 176:
			for i in range(80):
				kdo_vyhral.append("tym_1")
			for i in range(20):
				kdo_vyhral.append("tym_2")
		elif rozdil_ratingu <= 240:
			for i in range(85):
				kdo_vyhral.append("tym_1")
			for i in range(15):
				kdo_vyhral.append("tym_2")
		elif rozdil_ratingu > 240:
			for i in range(90):
				kdo_vyhral.append("tym_1")
			for i in range(10):
				kdo_vyhral.append("tym_2")
	elif tym_2 > tym_1:
		silnejsi_tym = 2
		print(f"\nTým dva je silnější a rozdíl ratingů je {rozdil_ratingu}")
		if rozdil_ratingu <= 22:
			for i in range(50):
				kdo_vyhral.append("tym_2")
			for i in range(50):
				kdo_vyhral.append("tym_1")
		elif rozdil_ratingu <= 33:
			for i in range(55):
				kdo_vyhral.append("tym_2")
			for i in range(45):
				kdo_vyhral.append("tym_1")
		elif rozdil_ratingu <= 44:
			for i in range(60):
				kdo_vyhral.append("tym_2")
			for i in range(40):
				kdo_vyhral.append("tym_1")
		elif rozdil_ratingu <= 66:
			for i in range(65):
				kdo_vyhral.append("tym_2")
			for i in range(35):
				kdo_vyhral.append("tym_1")
		elif rozdil_ratingu <= 88:
			for i in range(70):
				kdo_vyhral.append("tym_2")
			for i in range(30):
				kdo_vyhral.append("tym_1")
		elif rozdil_ratingu <= 121:
			for i in range(75):
				kdo_vyhral.append("tym_2")
			for i in range(25):
				kdo_vyhral.append("tym_1")
		elif rozdil_ratingu <= 176:
			for i in range(80):
				kdo_vyhral.append("tym_2")
			for i in range(20):
				kdo_vyhral.append("tym_1")
		elif rozdil_ratingu <= 240:
			for i in range(85):
				kdo_vyhral.append("tym_2")
			for i in range(15):
				kdo_vyhral.append("tym_1")
		elif rozdil_ratingu > 240:
			for i in range(90):
				kdo_vyhral.append("tym_2")
			for i in range(10):
				kdo_vyhral.append("tym_1")
	else:
		print("\nOba týmy jsou stejně silné")
		for i in range(50):
				kdo_vyhral.append("tym_1")
		for i in range(50):
				kdo_vyhral.append("tym_2")


	random.shuffle(kdo_vyhral)
	vitez = random.choice(kdo_vyhral)

	if vitez == "tym_1":
		if silnejsi_tym == 0:
				vysledek = random.choice(vysledky_1)
		if silnejsi_tym == 1:
			if rozdil_ratingu <= 66:
				vysledek = random.choice(vysledky_1)
			elif rozdil_ratingu <= 110:
				vysledek = random.choice(vysledky_2)
			elif rozdil_ratingu <= 210:
				vysledek = random.choice(vysledky_3)
			elif rozdil_ratingu >= 210:
				vysledek = random.choice(vysledky_4)
		if silnejsi_tym == 2:
			vysledek = random.choice(vysledky_1)
	
	

	if vitez == "tym_2":
		if silnejsi_tym == 0:
				vysledek = random.choice(vysledky_1)
		if silnejsi_tym == 2:	
			if rozdil_ratingu <= 66:
				vysledek = random.choice(vysledky_1)
			elif rozdil_ratingu <= 110:
				vysledek = random.choice(vysledky_2)
			elif rozdil_ratingu <= 210:
				vysledek = random.choice(vysledky_3)
			elif rozdil_ratingu >= 210:
				vysledek = random.choice(vysledky_4)
		if silnejsi_tym == 1:
			vysledek = random.choice(vysledky_1)

	sleep(1)
	
#	for i in range(10000):
#		random.shuffle(kdo_vyhral)
#		vitez = random.choice(kdo_vyhral)
#		if vitez == "tym_1":
#			pocet_vyher_tym_1 += 1
#		elif vitez == "tym_2":
#			pocet_vyher_tym_2 += 1
#	print("tym 1: " + str(pocet_vyher_tym_1))
#	print("tym 2: " + str(pocet_vyher_tym_2))

	label_kdo_vyhral.config( text = "Výtěz: " + vitez + " poměrem: " + vysledek )









window.grid_rowconfigure(0, weight = 1)
window.grid_columnconfigure(0, weight = 1)


#hlavni strana na ktere bude vysledek
uvodni_strana = Frame(window, bg = "blue")
uvodni_strana.grid(row = 0, column = 0, sticky ="nsew")
uvodni_strana.grid_rowconfigure([0,1,2,3,4,5,6,7,8], weight = 1, minsize=25)
uvodni_strana.grid_columnconfigure([0,1,2], weight = 1, minsize=30)
label = tk.Label(uvodni_strana,text="Zápas").grid(row=0, column=1)
zadani_prvniho_tymu = tk.Button(uvodni_strana,text="zadat tým 1", command=zadani_tymu_1).grid(row=2, column=0)
zadani_druheho_tymu = tk.Button(uvodni_strana,text="zadat tým 2", command=zadani_tymu_2).grid(row=2, column=2)
label_rating_T1 = tk.Label(uvodni_strana, text="Rating týmu 1: " + str(rating_T1), width=19)
label_rating_T1.grid(row=3, column = 0)
label_rating_T2 = tk.Label(uvodni_strana, text="Rating týmu 2: " + str(rating_T2), width=19)#19
label_rating_T2.grid(row=3, column = 2)
label_rozdil = tk.Label(uvodni_strana, text="Rozdíl: " + str(rozdil))
label_rozdil.grid(row=4, column = 1)
label_kdo_vyhral = tk.Label(uvodni_strana, text = "Výtěz: " + vitez + " poměrem: " + vysledek , width=25)
label_kdo_vyhral.grid(row=6,column=1)
btn_vygeneruj_vysledek = tk.Button(uvodni_strana, text="Zobrazit výsledek", command=vygeneruj_vysledek)
btn_vygeneruj_vysledek.grid(row=7,column=1)


#stranka na zadani Tymu 1
zadavani_T1 = Frame(window, bg = "red")
zadavani_T1.grid(row = 0, column = 0, sticky ="nsew")
zadavani_T1.grid_rowconfigure([0,1,2,3,4,5,6,7,8], weight = 1, minsize=25)
zadavani_T1.grid_columnconfigure([0,1,2,3,4,5,6], weight = 1, minsize=30)
nazev_T1 = tk.Label(zadavani_T1, text="Tým 1")
nazev_T1.grid(row=0,column=3)



#hráč 1
lbl_T1_1 = tk.Label(zadavani_T1, text="hráč 1")
lbl_T1_1.grid(row=1,column=0)
entry_T1_1 = tk.Entry(zadavani_T1, width= 5)
entry_T1_1.grid(row=1,column=1)
var_chck_T1_1 = tk.IntVar()
chckb_T1_1 = tk.Checkbutton(zadavani_T1, variable=var_chck_T1_1, onvalue=1,offvalue=0)
chckb_T1_1.grid(row=1,column=2)

#hráč 2
lbl_T1_2 = tk.Label(zadavani_T1, text="hráč 2")
lbl_T1_2.grid(row=2,column=0)
entry_T1_2 = tk.Entry(zadavani_T1, width= 5)
entry_T1_2.grid(row=2,column=1)
var_chck_T1_2 = tk.IntVar()
chckb_T1_2 = tk.Checkbutton(zadavani_T1, variable=var_chck_T1_2, onvalue=1,offvalue=0)
chckb_T1_2.grid(row=2,column=2)

#hráč 3
lbl_T1_3 = tk.Label(zadavani_T1, text="hráč 3")
lbl_T1_3.grid(row=3,column=0)
entry_T1_3 = tk.Entry(zadavani_T1, width= 5)
entry_T1_3.grid(row=3,column=1)
var_chck_T1_3 = tk.IntVar()
chckb_T1_3 = tk.Checkbutton(zadavani_T1, variable=var_chck_T1_3, onvalue=1,offvalue=0)
chckb_T1_3.grid(row=3,column=2)

#hráč 4
lbl_T1_4 = tk.Label(zadavani_T1, text="hráč 4")
lbl_T1_4.grid(row=4,column=0)
entry_T1_4 = tk.Entry(zadavani_T1, width= 5)
entry_T1_4.grid(row=4,column=1)
var_chck_T1_4 = tk.IntVar()
chckb_T1_4 = tk.Checkbutton(zadavani_T1, variable=var_chck_T1_4, onvalue=1,offvalue=0)
chckb_T1_4.grid(row=4,column=2)

#hráč 5
lbl_T1_5 = tk.Label(zadavani_T1, text="hráč 5")
lbl_T1_5.grid(row=5,column=0)
entry_T1_5 = tk.Entry(zadavani_T1, width= 5)
entry_T1_5.grid(row=5,column=1)
var_chck_T1_5 = tk.IntVar()
chckb_T1_5 = tk.Checkbutton(zadavani_T1, variable=var_chck_T1_5, onvalue=1,offvalue=0)
chckb_T1_5.grid(row=5,column=2)

#hráč 6
lbl_T1_6 = tk.Label(zadavani_T1, text="hráč 6")
lbl_T1_6.grid(row=6,column=0)
entry_T1_6 = tk.Entry(zadavani_T1, width= 5)
entry_T1_6.grid(row=6,column=1)
var_chck_T1_6 = tk.IntVar()
chckb_T1_6 = tk.Checkbutton(zadavani_T1, variable=var_chck_T1_6, onvalue=1,offvalue=0)
chckb_T1_6.grid(row=6,column=2)

#hráč 7
lbl_T1_7 = tk.Label(zadavani_T1, text="hráč 7")
lbl_T1_7.grid(row=1,column=4)
entry_T1_7 = tk.Entry(zadavani_T1, width= 5)
entry_T1_7.grid(row=1,column=5)
var_chck_T1_7 = tk.IntVar()
chckb_T1_7 = tk.Checkbutton(zadavani_T1, variable=var_chck_T1_7, onvalue=1,offvalue=0)
chckb_T1_7.grid(row=1,column=6)

#hráč 8
lbl_T1_8 = tk.Label(zadavani_T1, text="hráč 8")
lbl_T1_8.grid(row=2,column=4)
entry_T1_8 = tk.Entry(zadavani_T1, width= 5)
entry_T1_8.grid(row=2,column=5)
var_chck_T1_8 = tk.IntVar()
chckb_T1_8 = tk.Checkbutton(zadavani_T1, variable=var_chck_T1_8, onvalue=1,offvalue=0)
chckb_T1_8.grid(row=2,column=6)

#hráč 9
lbl_T1_9 = tk.Label(zadavani_T1, text="hráč 9")
lbl_T1_9.grid(row=3,column=4)
entry_T1_9 = tk.Entry(zadavani_T1, width= 5)
entry_T1_9.grid(row=3,column=5)
var_chck_T1_9 = tk.IntVar()
chckb_T1_9 = tk.Checkbutton(zadavani_T1, variable=var_chck_T1_9, onvalue=1,offvalue=0)
chckb_T1_9.grid(row=3,column=6)

#hráč 10
lbl_T1_10 = tk.Label(zadavani_T1, text="hráč 10")
lbl_T1_10.grid(row=4,column=4)
entry_T1_10 = tk.Entry(zadavani_T1, width= 5)
entry_T1_10.grid(row=4,column=5)
var_chck_T1_10 = tk.IntVar()
chckb_T1_10 = tk.Checkbutton(zadavani_T1, variable=var_chck_T1_10, onvalue=1,offvalue=0)
chckb_T1_10.grid(row=4,column=6)

#hráč 11
lbl_T1_11 = tk.Label(zadavani_T1, text="hráč 11")
lbl_T1_11.grid(row=5,column=4)
entry_T1_11 = tk.Entry(zadavani_T1, width= 5)
entry_T1_11.grid(row=5,column=5)
var_chck_T1_11 = tk.IntVar()
chckb_T1_11 = tk.Checkbutton(zadavani_T1, variable=var_chck_T1_11, onvalue=1,offvalue=0)
chckb_T1_11.grid(row=5,column=6)


zpet_na_uvodni_stranu = tk.Button(zadavani_T1, text = "potvrdit", command=ukaz_uvodni_stranu_tym_1).grid(row = 8, column= 4)


#stranka na zadani Tymu 2
zadavani_T2 = Frame(window, bg = "red")
zadavani_T2.grid(row = 0, column = 0, sticky ="nsew")
zadavani_T2.grid_rowconfigure([0,1,2,3,4,5,6,7,8], weight = 1, minsize=25)
zadavani_T2.grid_columnconfigure([0,1,2,3,4,5,6], weight = 1, minsize=30)
nazev_T2 = tk.Label(zadavani_T2, text="Tým 2")
nazev_T2.grid(row=0,column=3)



#hráč 1
lbl_T2_1 = tk.Label(zadavani_T2, text="hráč 1")
lbl_T2_1.grid(row=1,column=0)
entry_T2_1 = tk.Entry(zadavani_T2, width= 5)
entry_T2_1.grid(row=1,column=1)
var_chck_T2_1 = tk.IntVar()
chckb_T2_1 = tk.Checkbutton(zadavani_T2, variable=var_chck_T2_1, onvalue=1,offvalue=0)
chckb_T2_1.grid(row=1,column=2)

#hráč 2
lbl_T2_2 = tk.Label(zadavani_T2, text="hráč 2")
lbl_T2_2.grid(row=2,column=0)
entry_T2_2 = tk.Entry(zadavani_T2, width= 5)
entry_T2_2.grid(row=2,column=1)
var_chck_T2_2 = tk.IntVar()
chckb_T2_2 = tk.Checkbutton(zadavani_T2, variable=var_chck_T2_2, onvalue=1,offvalue=0)
chckb_T2_2.grid(row=2,column=2)

#hráč 3
lbl_T2_3 = tk.Label(zadavani_T2, text="hráč 3")
lbl_T2_3.grid(row=3,column=0)
entry_T2_3 = tk.Entry(zadavani_T2, width= 5)
entry_T2_3.grid(row=3,column=1)
var_chck_T2_3 = tk.IntVar()
chckb_T2_3 = tk.Checkbutton(zadavani_T2, variable=var_chck_T2_3, onvalue=1,offvalue=0)
chckb_T2_3.grid(row=3,column=2)

#hráč 4
lbl_T2_4 = tk.Label(zadavani_T2, text="hráč 4")
lbl_T2_4.grid(row=4,column=0)
entry_T2_4 = tk.Entry(zadavani_T2, width= 5)
entry_T2_4.grid(row=4,column=1)
var_chck_T2_4 = tk.IntVar()
chckb_T2_4 = tk.Checkbutton(zadavani_T2, variable=var_chck_T2_4, onvalue=1,offvalue=0)
chckb_T2_4.grid(row=4,column=2)

#hráč 5
lbl_T2_5 = tk.Label(zadavani_T2, text="hráč 5")
lbl_T2_5.grid(row=5,column=0)
entry_T2_5 = tk.Entry(zadavani_T2, width= 5)
entry_T2_5.grid(row=5,column=1)
var_chck_T2_5 = tk.IntVar()
chckb_T2_5 = tk.Checkbutton(zadavani_T2, variable=var_chck_T2_5, onvalue=1,offvalue=0)
chckb_T2_5.grid(row=5,column=2)

#hráč 6
lbl_T2_6 = tk.Label(zadavani_T2, text="hráč 6")
lbl_T2_6.grid(row=6,column=0)
entry_T2_6 = tk.Entry(zadavani_T2, width= 5)
entry_T2_6.grid(row=6,column=1)
var_chck_T2_6 = tk.IntVar()
chckb_T2_6 = tk.Checkbutton(zadavani_T2, variable=var_chck_T2_6, onvalue=1,offvalue=0)
chckb_T2_6.grid(row=6,column=2)

#hráč 7
lbl_T2_7 = tk.Label(zadavani_T2, text="hráč 7")
lbl_T2_7.grid(row=1,column=4)
entry_T2_7 = tk.Entry(zadavani_T2, width= 5)
entry_T2_7.grid(row=1,column=5)
var_chck_T2_7 = tk.IntVar()
chckb_T2_7 = tk.Checkbutton(zadavani_T2, variable=var_chck_T2_7, onvalue=1,offvalue=0)
chckb_T2_7.grid(row=1,column=6)

#hráč 8
lbl_T2_8 = tk.Label(zadavani_T2, text="hráč 8")
lbl_T2_8.grid(row=2,column=4)
entry_T2_8 = tk.Entry(zadavani_T2, width= 5)
entry_T2_8.grid(row=2,column=5)
var_chck_T2_8 = tk.IntVar()
chckb_T2_8 = tk.Checkbutton(zadavani_T2, variable=var_chck_T2_8, onvalue=1,offvalue=0)
chckb_T2_8.grid(row=2,column=6)

#hráč 9
lbl_T2_9 = tk.Label(zadavani_T2, text="hráč 9")
lbl_T2_9.grid(row=3,column=4)
entry_T2_9 = tk.Entry(zadavani_T2, width= 5)
entry_T2_9.grid(row=3,column=5)
var_chck_T2_9 = tk.IntVar()
chckb_T2_9 = tk.Checkbutton(zadavani_T2, variable=var_chck_T2_9, onvalue=1,offvalue=0)
chckb_T2_9.grid(row=3,column=6)

#hráč 10
lbl_T2_10 = tk.Label(zadavani_T2, text="hráč 10")
lbl_T2_10.grid(row=4,column=4)
entry_T2_10 = tk.Entry(zadavani_T2, width= 5)
entry_T2_10.grid(row=4,column=5)
var_chck_T2_10 = tk.IntVar()
chckb_T2_10 = tk.Checkbutton(zadavani_T2, variable=var_chck_T2_10, onvalue=1,offvalue=0)
chckb_T2_10.grid(row=4,column=6)

#hráč 11
lbl_T2_11 = tk.Label(zadavani_T2, text="hráč 11")
lbl_T2_11.grid(row=5,column=4)
entry_T2_11 = tk.Entry(zadavani_T2, width= 5)
entry_T2_11.grid(row=5,column=5)
var_chck_T2_11 = tk.IntVar()
chckb_T2_11 = tk.Checkbutton(zadavani_T2, variable=var_chck_T2_11, onvalue=1,offvalue=0)
chckb_T2_11.grid(row=5,column=6)


zpet_na_uvodni_stranu = tk.Button(zadavani_T2, text = "potvrdit", command=ukaz_uvodni_stranu_tym_2).grid(row = 8, column= 4)




ukaz_uvodni_stranu_start()

window.mainloop()
import random
from time import sleep

kdo_vyhral = []
# pocet_vyher_tym_1 = 0
# pocet_vyher_tym_2 = 0
tym_1 = 0
tym_2 = 0
silnejsi_tym = 0
vysledek = ""
vysledky_1 = ["1:0", "1:0", "1:0", "2:0", "2:0", "2:1", "2:1", "2:1", "3:1", "3:2", "3:2", "4:3", "5:4", "5:3", "6:4", "6:5"]
vysledky_2 = ["1:0", "3:1", "3:1", "3:1", "4:1", "2:0", "2:0", "2:0", "3:0", "4:1", "4:2", "4:2", "5:2", "5:4", "5:3", "6:3", "7:4", ]
vysledky_3 = ["3:0", "3:0", "4:0", "4:0", "3:0", "3:1", "2:0", "5:0", "5:1", "5:1", "4:1", "4:1", "6:0", "6:1", "6:1", "6:2", "6:2", "6:2", "6:3", "6:3"]



print("\n\n\nPRVNÍ TÝM:")
for i in range(1, 12):
	hrac_tym_1 = int(input("\nZadejte hráče číslo " + str(i) + ":"))
	pozice = input(f"Je tento hráč na své pozici?")
	if pozice == "ano" or pozice == "Ano" or pozice == "Je" or pozice == "je" or pozice == "a" or pozice == "A":
		tym_1 = tym_1 + hrac_tym_1
	else:
		tym_1 = tym_1 + (hrac_tym_1 * 0.8)
		
print("\n\nDRUHÝ TÝM:")

for i in range(1, 12):
	hrac_tym_2 = int(input("\nZadejte hráče číslo " + str(i) + ":"))
	pozice = input(f"Je tento hráč na své pozici?")
	if pozice == "ano" or pozice == "Ano" or pozice == "Je" or pozice == "je" or pozice == "a" or pozice == "A":
		tym_2 = tym_2 + hrac_tym_2
	else:
		tym_2 = tym_2 + (hrac_tym_2 * 0.8)


rozdil_ratingu = abs(tym_1 - tym_2)

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
		elif rozdil_ratingu >= 110:
			vysledek = random.choice(vysledky_3)
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
		else:
			vysledek = random.choice(vysledky_3)
	if silnejsi_tym == 1:
		vysledek = random.choice(vysledky_1)

sleep(5)

# for i in range(10000):
# 	random.shuffle(kdo_vyhral)
# 	vitez = random.choice(kdo_vyhral)
# 	if vitez == "tym_1":
# 		pocet_vyher_tym_1 += 1
# 	elif vitez == "tym_2":
# 		pocet_vyher_tym_2 += 1

print(f"\nVyhrál {vitez} poměrem {vysledek}\n\n")

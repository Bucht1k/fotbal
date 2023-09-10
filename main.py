import random
kdo_vyhral=[]
pocet_vyher_tym_1 = 0
pocet_vyher_tym_2 = 0
tym_1= 0
tym_2 = 0
print("zadejte rating hracu prvniho tymu:")
for i in range(5):
	hrac_tym_1 = int(input("zadejte hrace tymu 1 cislo" + str(i) + ": "))
	tym_1 = tym_1 + hrac_tym_1
print("zadejte rating hracu druheho tymu:")
for i in range(5):
	hrac_tym_2 = int(input("zadejte hrace tymu 2 cislo" + str(i) + ": "))
	tym_2 = tym_2 + hrac_tym_2
#tym_1 = int(input("zadejte rating prvniho tymu: "))
#tym_2 = int(input("zadejte rating duheho tymu: "))
rozdil_ratingu= abs(tym_1 - tym_2)
print(rozdil_ratingu)
if tym_1>tym_2:
	print("tym 1 je silnejsi")
	if rozdil_ratingu <=10:
		for i in range(50):
			kdo_vyhral.append("tym_1")
		for i in range(50):
			kdo_vyhral.append("tym_2")
	if rozdil_ratingu <=20 and rozdil_ratingu >10:
		for i in range(55):
			kdo_vyhral.append("tym_1")
		for i in range(45):
			kdo_vyhral.append("tym_2")
	if rozdil_ratingu <=30 and rozdil_ratingu >20:
		for i in range(60):
			kdo_vyhral.append("tym_1")
		for i in range(40):
			kdo_vyhral.append("tym_2")
	if rozdil_ratingu <=40 and rozdil_ratingu >30:
		for i in range(65):
			kdo_vyhral.append("tym_1")
		for i in range(35):
			kdo_vyhral.append("tym_2")
	if rozdil_ratingu <=50 and rozdil_ratingu > 40:
		for i in range(70):
			kdo_vyhral.append("tym_1")
		for i in range(30):
			kdo_vyhral.append("tym_2")
	if rozdil_ratingu <=60 and rozdil_ratingu > 50:
		for i in range(75):
			kdo_vyhral.append("tym_1")
		for i in range(25):
			kdo_vyhral.append("tym_2")
	if rozdil_ratingu <=70 and rozdil_ratingu > 60:
		for i in range(80):
			kdo_vyhral.append("tym_1")
		for i in range(20):
			kdo_vyhral.append("tym_2")
	if rozdil_ratingu <=80 and rozdil_ratingu > 70:
		for i in range(85):
			kdo_vyhral.append("tym_1")
		for i in range(15):
			kdo_vyhral.append("tym_2")
	if rozdil_ratingu > 80:
		for i in range(90):
			kdo_vyhral.append("tym_1")
		for i in range(10):
			kdo_vyhral.append("tym_2")
elif tym_2 > tym_1:
	print("tym 2 je silnejsi")
	if rozdil_ratingu <=10:
		for i in range(50):
			kdo_vyhral.append("tym_2")
		for i in range(50):
			kdo_vyhral.append("tym_1")
	if rozdil_ratingu <=20 and rozdil_ratingu >10:
		for i in range(55):
			kdo_vyhral.append("tym_2")
		for i in range(45):
			kdo_vyhral.append("tym_1")
	if rozdil_ratingu <=30 and rozdil_ratingu >20:
		for i in range(60):
			kdo_vyhral.append("tym_2")
		for i in range(40):
			kdo_vyhral.append("tym_1")
	if rozdil_ratingu <=40 and rozdil_ratingu >30:
		for i in range(65):
			kdo_vyhral.append("tym_2")
		for i in range(35):
			kdo_vyhral.append("tym_1")
	if rozdil_ratingu <=50 and rozdil_ratingu > 40:
		for i in range(70):
			kdo_vyhral.append("tym_2")
		for i in range(30):
			kdo_vyhral.append("tym_1")
	if rozdil_ratingu <=60 and rozdil_ratingu > 50:
		for i in range(75):
			kdo_vyhral.append("tym_2")
		for i in range(25):
			kdo_vyhral.append("tym_1")
	if rozdil_ratingu <=70 and rozdil_ratingu > 60:
		for i in range(80):
			kdo_vyhral.append("tym_2")
		for i in range(20):
			kdo_vyhral.append("tym_1")
	if rozdil_ratingu <=80 and rozdil_ratingu > 70:
		for i in range(85):
			kdo_vyhral.append("tym_2")
		for i in range(15):
			kdo_vyhral.append("tym_1")
	if rozdil_ratingu > 80:
		for i in range(90):
			kdo_vyhral.append("tym_2")
		for i in range(10):
			kdo_vyhral.append("tym_1")
else:
	print("oba tymy jsou stejne silne")
	for i in range(50):
			kdo_vyhral.append("tym_1")
	for i in range(50):
			kdo_vyhral.append("tym_2")
print(kdo_vyhral)
for i in range(10000):
	random.shuffle(kdo_vyhral)
	vitez = random.choice(kdo_vyhral)
	if vitez == "tym_1":
		pocet_vyher_tym_1 += 1
	elif vitez == "tym_2":
		pocet_vyher_tym_2 += 1
print("pocet vyher tymu 1: " + str(pocet_vyher_tym_1))
#print(pocet_vyher_tym_1)
print("pocet vyher tymu 2: " + str(pocet_vyher_tym_2))
#print(pocet_vyher_tym_2)
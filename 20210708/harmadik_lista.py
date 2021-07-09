# Adott két lista amiből egy harmadikat kell csinálni, úgy ,hogy az első listából a páratlan indexű elemeket a másodikból a páros indexű elemeket tartalmazza
# PL:

listOne = [3, 6, 9, 12, 15, 18, 21]
listTwo = [4, 8, 12, 16, 20, 24, 28]

# Expected Output:

# Element at odd-index positions from list one
# [6, 12, 18]
# Element at even-index positions from list two
# [4, 12, 20, 28]
# Printing Final third list
# [6, 12, 18, 4, 12, 20, 28]

oddList = []
evenList = []

for i, v in enumerate(listOne):
    if i % 2 != 0:
        oddList.append(v)
for i, v in enumerate(listTwo):
    if i % 2 == 0:
        evenList.append(v)
finalList = oddList + evenList
print(finalList)

# Erika
# istOne = [3, 6, 9, 12, 15, 18, 21]
# listTwo = [4, 8, 12, 16, 20, 24, 28]
# eredmeny = []  # azért, mert kell egy harmadik lista a feladat szerint
# for i, v in enumerate(listOne):
#     if i % 2 != 0:
#         #print(i, v) Ellenőrzésre jó
#         eredmeny.append(v)
# print(eredmeny)   # részeredmény ellenőrzés
# j = len(eredmeny)  # a kapott eredményt eltároljuk egy változóba
# for i, v in enumerate(listTwo):
#     if i % 2 == 0:
#         #print(i, v)
#         eredmeny.append(v)
# print(eredmeny[j:])  # itt meghívjuk az első listáből készített új listát
# print(eredmeny)  # kiírja a végeredményt


# ez mástól

# ez nem megy és csak indexxel sem

# listOne = [3, 6, 9, 12, 15, 18, 21]
# listTwo = [4, 8, 12, 16, 20, 24, 28]
# mixed_list = []
# for i, v in enumerate(listOne):
#    if listOne.index(i) % 2 == 1:
#        mixed_list += listOne[i]
#for j, w in enumerate(listTwo):
#    if listTwo.index(i) % 2 == 0:
#        mixed_list += listTwo[i]
# print(mixed_list)
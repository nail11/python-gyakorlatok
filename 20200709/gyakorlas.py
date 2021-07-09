# írj egy Python függvényt ami megszámolja a magánhangzókat egy paraméterül kapott szóban
# A programodban teszteld le a függvényt. Az ismert magánhangzók listája: `aAeEiIoOuU`
# Bemenet: 'hello'
# Kimenet: 2

# ez jó megoldás, de más mint a konzultáción

# def maganhangzo(szo):
#
#     maganhangzok = 'aAeEiIoOuU'
#     db = 0
#
#     for s in szo:
#         for mh in maganhangzok:
#             if s == mh:
#                 db += 1
#     print(db)


# ez a konzultációs megoldás

szo = 'ieouo'

def maganhangzo(szo):

    maganhangzok = 'aAeEiIoOuU'
    db = 0

    for betu in szo:
        if betu in maganhangzok:
            db += 1
    print(db)

# meghívom a függvényt

maganhangzo(szo)
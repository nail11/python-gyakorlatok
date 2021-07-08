# írjunk olyan Python függvényt, ahol bekérünk egy pozitív egész számot,
# és kiírjuk a kimentere, hogy hány bárányunk van.
# Example:
# input = 3
# print out : 1 sheep...2 sheep...3 sheep...

def sheep_counter():
    n = int(input('Adj meg egy számot: '))
    l = list(range((n + 1)))

    for i in l[1: len(l) + 1]:
        print(str(i) + ' bárány', end='...')


sheep_counter()

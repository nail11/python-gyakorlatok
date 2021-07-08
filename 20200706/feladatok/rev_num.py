# írjunk olyan Python függvényt, ahol bekérünk egy pozitív egész számot,
# és kiírjuk a kimenetre a számot fordított lista formájában.
# Example:
# input = 123456
# print out : [6, 5, 4, 3, 2, 1]


def rev_num():
    num = input('Adj meg egy többjegyű számot: ')
    num_list = list(num)
    print('A fordított lista: '+ str(num_list[::-1]))

rev_num()
# Az alábbi mintát jelenítsd meg for ciklus segítségével!
# Minta:
# 5 4 3 2 1
# 4 3 2 1
# 3 2 1
# 2 1
# 1

list = [1, 2, 3, 4, 5]
list_rev = list[::-1]

for j in range(5):
    for i in list_rev[j:]:
        print(i, end='')
    print()

# oszlop - ez nem megy

# fx = [5, 4, 3, 2, 1]
# y = []
# for j in range(5):
#     y.append(x[j:])
# print(y)
# for idx, i in enumerate(y):
#     for k in range(len(i)):
#         print(y[idx][k], end=' ')
#     print()

# ez megy

# x = [5, 4, 3, 2, 1]
# y = []
# for j in range(5):
#          y.append(x[j:])
#          for i in y:
#              print(*i)

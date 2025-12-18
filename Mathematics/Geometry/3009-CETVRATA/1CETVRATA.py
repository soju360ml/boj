list_1 = list()
dict_x = dict()
dict_y = dict()

for i in range(3):
    list_1.append(list(map(int, input().split())))

dict_x[list_1[0][0]] = 1
dict_y[list_1[0][1]] = 1

for i in list_1[1:]:
    if i[0] in dict_x:
        dict_x[i[0]] += 1
    else:
        dict_x[i[0]] = 1
    if i[1] in dict_y:
        dict_y[i[1]] += 1
    else:
        dict_y[i[1]] = 1

for k, v in dict_x.items():
    if v == 1: x = k

for k, v in dict_y.items():
    if v == 1: y = k

print(x, y)
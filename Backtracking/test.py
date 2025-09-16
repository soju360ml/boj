list_1 = list(range(2))

print(list_1)

for i, v in enumerate(list_1):
    print(i, v)
    a = list_1.pop(i)
    list_1.append(v)

print(list_1)
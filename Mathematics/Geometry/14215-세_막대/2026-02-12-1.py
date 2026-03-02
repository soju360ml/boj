a, b, c = map(int, input().split())

lst = list((a, b, c))

lst.sort()

if lst[2] >= lst[0] + lst[1]:
    print((lst[0] + lst[1]) * 2 - 1)
else:
    print(sum(lst))
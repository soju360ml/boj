N = list(map(int, input().split()))
Aflag = 0
Dflag = 0

for j, i in enumerate(N):
    if j == 0:
        if i == 1:
            Aflag = 1
        elif i == 8:
            Dflag = 1
    if Aflag == 1:
        if j + 1 == i:
            continue
        else:
            Aflag = 0
    elif Dflag == 1:
        if j == 8 - i:
            continue
        else:
            Dflag = 0
    else:
        print('mixed')
        break

if Aflag == 1:
    print('ascending')
elif Dflag == 1:
    print('descending')
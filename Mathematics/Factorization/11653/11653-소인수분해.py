N = int(input())

def func_1(n):
    dict_1 = {}
    i = 2
    
    while i <= n:
        if n % i == 0:
            if i not in dict_1:
                dict_1[i] = 1
            else:
                dict_1[i] += 1
            n /= i
            continue
        else:
            i += 1
    return dict_1

for key, item in func_1(N).items():
    for i in range(item):
        print(key)
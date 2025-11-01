N = int(input())
A = sorted(list(map(int, input().split())))

M = int(input())
B = tuple(map(int, input().split()))

def Bsearch(source, target):
    left = 0
    right = len(source) - 1

    while left <= right:
        center = (left + right) // 2
        guess = source[center]

        if target == guess:
            return True
        elif target < guess:
            right = center - 1
        elif target > guess:
            left = center + 1
    return False

for i in B:
    result = Bsearch(A, i)
    if result == True:
        print(1)
    else:
        print(0)
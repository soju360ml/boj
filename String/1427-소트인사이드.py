N = input()
numList = [int(i) for i in N]
numList.sort(reverse=True)
print(''.join(map(str, numList)))
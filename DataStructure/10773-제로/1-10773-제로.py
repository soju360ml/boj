K = int(input())
myStack = []

for _ in range(K):
    curValue = int(input())
    if curValue == 0:
        if len(myStack) > 0:
            myStack.pop()
    else:
        myStack.append(curValue)

print(sum(myStack))
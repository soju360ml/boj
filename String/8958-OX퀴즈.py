T = int(input())
scoreTable = []
for _ in range(T):
    s = input()
    score = 0
    seq = 0
    for i in s:
        if i == 'O':
            seq += 1
            score += seq
        else:
            seq = 0
    scoreTable.append(score)

for i in scoreTable:
    print(i)
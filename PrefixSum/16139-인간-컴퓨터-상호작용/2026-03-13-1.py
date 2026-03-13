import sys;read = sys.stdin.readline

S = read().strip()
Sset = set()
# 서브태스크2: 문자열의 길이가 2천 이상인 경우 알파벳26개를 넘어가면 모든 알파벳이 사용되므로 그 즉시 break한다
for i in S:
    if len(Sset) == 26:
        break
    Sset.add(i)
    
q = int(read())

# print(f'{S}의 길이는 {len(S)}')

Q = [None] * q
for i in range(q):
    c, left, right = read().split()
    left, right = map(lambda x: int(x) + 1, (left, right))
    Q[i] = (c, left, right)

s = set()
for i in Q:
    if len(s) == 26:
        break
    s.add(i[0])
    
    
alpha1 = {i: [0] * (len(S) + 1) for i in s if i in Sset}
# print(alpha1)

for i in alpha1:
    for j in range(1, len(S) + 1):
        if S[j - 1] == i:
            # print(f'{j - 1}번 문자는 {i}라서 1 추가합니다')
            alpha1[i][j] = alpha1[i][j - 1] + 1
        else:
            alpha1[i][j] = alpha1[i][j - 1]
# print(alpha1)

for i in Q:
    c = i[0]
    left, right = i[1], i[2]
    if c not in Sset:
        print(0)
    else:
        print(alpha1[c][right] - alpha1[c][left - 1])
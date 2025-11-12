memo = {}
s = []

def w(a, b, c):
    # 딕셔너리 get함수를 사용하는 이유: 키가 존재하면 값, 키가 존재하지 않으면 None을 반환(에러를 일으키지 않게 하기 위해)
    # all()을 사용하는 이유: all은 iterable을 전달받아 모든 and연산을 한다(모두 True면 True)
    # if all(memo.get(a), memo[a].get(b), memo[a][b].get(c)): # 잘돗된 용법
    if memo.get(a) and memo[a].get(b) and memo[a][b].get(c):
        return memo[a][b][c]
    else:
        if memo.get(a) is None:
            memo[a] = {b: {c: None}}
        elif memo[a].get(b) is None:
            memo[a][b] = {}
            
        if any(map(lambda x: x <= 0, (a, b, c))):
            memo[a][b][c] = 1
        elif any(map(lambda x: x > 20, (a, b, c))):
            memo[a][b][c] = w(20, 20, 20)
        elif a < b and b < c:
            memo[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        else:
            memo[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
            # 111 -> 011 + 001 + 010 - 000
            # 011 -> -111 + -101 + -110 - -100
        return memo[a][b][c]
    

while True:
    N = tuple(map(int, input().split()))

    if all(map(lambda x: x == -1, N)):
        break
    else:
        s.append(f'w({N[0]}, {N[1]}, {N[2]}) = {w(*N)}')

for i in s:
    print(i)
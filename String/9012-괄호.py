# 리스트의 값이 str이므로 join메소드를 통해 subscripting을 한다.

T = int(input())

result = []
for _ in range(T):
    s = input()
    isvps = None
    stack = 0
    for i in s:
        if i == '(':
            stack += 1
        else:
            stack -= 1
            if stack < 0:
                isvps = False
                break
    if stack == 0:
        isvps = True
    result.append('YES' if isvps else 'NO')

print('\n'.join(result))
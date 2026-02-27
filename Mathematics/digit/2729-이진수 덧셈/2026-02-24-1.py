T = int(input())

def solve(num):
    num = str(num)
    ans = ''
    nxt = 0
    for i in num[::-1]:
        cur = nxt + int(i)
        if cur < 2:
            ans = str(cur) + ans
            nxt = 0
        else:
            if cur == 2:
                ans = '0' + ans
            elif cur == 3:
                ans = '1' + ans
            nxt = 1

    if nxt == 1:
        ans = str(nxt) + ans

    return ans

for _ in range(T):
    n1, n2 = map(int, input().split())
    print(solve(n1 + n2))
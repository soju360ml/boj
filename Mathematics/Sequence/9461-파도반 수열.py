T = int(input())
memo = {
    1: 1,
    2: 1,
    3: 1,
    4: 2,
    5: 2
}
result = []
def P(n):
    if n in memo:
        return memo[n]
    else:
        memo[n] = P(n - 1) + P(n - 5)
        return memo[n]
for _ in range(T):
    N = int(input())
    result.append(P(N))
for i in result:
    print(i)
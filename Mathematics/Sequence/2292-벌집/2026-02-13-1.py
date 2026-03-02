N = int(input())

cnt = 1
ans = 1

while cnt < N:
    cnt += ans * 6
    ans += 1

print(ans)
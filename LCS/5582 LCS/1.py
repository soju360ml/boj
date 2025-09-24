import sys
input = sys.stdin.readline

str1 = input().strip()
str2 = input().strip()
prev_dp = [0] * len(str2)
max = 0

for i, c1 in enumerate(str1):
    cur_dp = [0] * len(str2)
    for j, c2 in enumerate(str2):
        if c1 == c2:
            if j == 0:
                cur_dp[j] = 1
            else:
                cur_dp[j] = prev_dp[j - 1] + 1
            if max < cur_dp[j]:
                max = cur_dp[j]
    prev_dp = cur_dp

print(max)
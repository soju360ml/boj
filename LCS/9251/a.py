import sys
input = sys.stdin.readline

str1 = input().strip()
str2 = input().strip()
prev_dp = [0] * (len(str2) + 1)
maxCount = 0

for i in range(1, len(str1) + 1):
    cur_dp = [0] * (len(str2) + 1)
    for j in range(1, len(str2) + 1):
        if str1[i - 1] != str2[j - 1]:
            cur_dp[j] = max(prev_dp[j], cur_dp[j - 1])
        else:
            cur_dp[j] = prev_dp[j - 1] + 1
        maxCount = max(maxCount, cur_dp[j])
    prev_dp = cur_dp

print(maxCount)
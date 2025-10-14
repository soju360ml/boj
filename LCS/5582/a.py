import sys
input = sys.stdin.readline

str1 = input().strip()
str2 = input().strip()
prev_dp = [0] * len(str2)
max = 0

for i in range(1, len(str1)):
    cur_dp = [0] * len(str2)
    for j in range(1, len(str2)):
        if str1[i - 1] == str2[j - 1]:
            if j == 0:
                cur_dp[j] = 1
            else:
                cur_dp[j] = prev_dp[j - 1] + 1
            if max < cur_dp[j]:
                max = cur_dp[j]
    prev_dp = cur_dp

print(max)
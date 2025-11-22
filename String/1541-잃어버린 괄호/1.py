s = input()
p = 0
sum = 0
p = s.find('-')
j = 0
mFlag = False

# -가 존재함
if p != -1:
    mFlag = True
# 모든 식이 +이므로 피벗은 문자열의 길이임
else:
    p = len(s)

# -가 있든 없든 피벗까지는 모두 더함
for i in range(p):
    if s[i] == '+':
        sum += int(s[j:i])
        j = i + 1
        continue
    if i == p - 1:
        sum += int(s[j:p])

j = p + 1
if mFlag is True:
    for i in range(p + 1, len(s)):
        if s[i] == '-' or s[i] == '+':
            sum -= int(s[j:i])
            j = i + 1
        elif i == len(s) - 1:
            sum -= int(s[j:i + 1])
            
print(sum)
import sys
input = sys.stdin.readline

def recursion(s, l, r, depth):
    if l >= r: return 1, depth
    elif s[l] != s[r]: return 0, depth
    else: return recursion(s, l+1, r-1, depth + 1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1, 1)

T = int(input())
string_ = [input().strip() for _ in range(T)]

for i in string_:
    iPalin = isPalindrome(i)
    print(iPalin[0], iPalin[1])

    스트립
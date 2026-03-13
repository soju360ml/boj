import sys ; read = sys.stdin.readline
import bisect
inp = read().strip()
arr = [[] for _ in range(26)]
for i in range(len(inp)):
    arr[ord(inp[i])-97].append(i)
    
for _ in range(int(read())):
    a,b,c = read().split()
    a = ord(a)-97
    b,c = int(b),int(c)
    print(bisect.bisect_right(arr[a],c)-bisect.bisect_left(arr[a],b))
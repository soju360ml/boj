import sys
input = sys.stdin.readline

def dfs(r, l, N):
    path = 0
    impossible_x = set()
    
    for i, x in enumerate(r):
        impossible_x.add(x)
        px = x + l - i
        mx = x - (l - i)
        if 0 <= px < N:
            impossible_x.add(px)
        if 0 <= mx < N:
            impossible_x.add(mx)

    for i in range(N):
        if i in impossible_x:
            continue
        elif l == N - 1:
            path += 1
            continue
        r.append(i)
        path += dfs(r, l + 1, N)
        r.pop()
    return path
    

if __name__ == "__main__":
    N = int(input())
    
    path = 0
    r = []
    l = 0
    
    for i in range(N):
        r.append(i)
        path += dfs(r, l + 1, N)
        r.pop()
    print(path)
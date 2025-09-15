import sys
input = sys.stdin.readline

# r의 값 제외, r로부터 계산한 값 제외
def dfs(r, l, N):
    l += 1
    for i in range(N):
        if i in r: continue
        elif i == abs()
    

if __name__ == "__main__":
    N = int(input())
    
    path = 0
    r = [False * N for _ in range(N)]
    l = 1
    
    for _ in range(N):
        path += dfs(r, l, N)
    print(path)
N,M = map(int, input().split())
path = [ [] for _ in range(N+1) ]
for i in range(N):
    line = list(map(int, input().split()))
    for j in (line[1:]):
        path[i+1].append(j)
        
match = [0 for _ in range(M+1)]    
def DFS(node):
    if visited[node] == 1:
        return False
    
    visited[node]=1
    
    for next in path[node]:
        if match[next] == 0 :
            match[next]=node
            return True
        
        else:
            before = match[next]
            if DFS(before) == True:
                match[next]=node
                return True
            
    return False
    

for i in range(1,N+1):
    visited=[0 for _ in range(N+1)]
    DFS(i)

sol=0
for i in range(M+1):
    if match[i]>0:
        sol+=1
print(sol)
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def match(adj, N, M):
    count = 0
    jobs = [False for _ in range(M)]
    for node in range(N):
        visited = [False for _ in range(M)]
        if dfs(adj, node, visited, jobs):
            count += 1
        if count == N or count == M:
            return count
    return count

def dfs(adj, node, visited, jobs):
    for job in adj[node]:
        job -= 1
        if visited[job] is False:
            visited[job] = True
            if jobs[job] is False or dfs(adj, jobs[job], visited, jobs):
                jobs[job] = node
                return True
    return False
        
if __name__ == "__main__":
    # N: 사람 수
    # M: 일의 개수
    N, M = input().split()
    N = int(N)
    M = int(M)

    """
    ex) adjacency = {
        1: [2, [A, B]],
        2: [2, [A, C]],
        3: [1, [C]]
        }
    """
    adjacency = []
    for i in range(N):
        # tmpInput = input().split()
        tmpInput = list(map(int, input().split()))
        adjacency.append(tmpInput[1:])
        
    print(match(adjacency, N, M))
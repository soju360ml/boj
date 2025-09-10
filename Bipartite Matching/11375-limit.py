import sys
input = sys.stdin.readline

def match(adj, jobs_count, N):
    count = 0
    jobs = [False for _ in range(jobs_count)]
    for node in range(len(adj)):
        visited = [False for _ in range(len(adj))]
        i = dfs(adj, node, visited, jobs)
        if i == True:
            count += 1
            # 모든 사람이 매칭된 경우, 모든 일자리가 매칭된 경우
        if count == N or count == jobs_count:
            return count
    return count

def dfs(adj, node, visited, jobs):
    if visited[node]:
        return False
    visited[node] = True
    for job in adj[node]:
        job -= 1
        if jobs[job] is False:
            jobs[job] = node
            return True
        else:
            who = jobs[job]
            result = dfs(adj, who, visited, jobs)
            if result:
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
        
    print(match(adjacency, M, N))
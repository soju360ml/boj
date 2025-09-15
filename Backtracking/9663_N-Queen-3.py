import sys
input = sys.stdin.readline

def dfs(col, row, possibleSet, distance_row, N):
    path = 0

    for attemptCol in possibleSet:
        flag = 0
        for i in distance_row:
            if i == attemptCol:
                flag = 1
                break
        if flag == 1: continue

        if row == N - 1:
            return 1
        
        else:
            possibleSet.remove(attemptCol)
            distance_row.append(abs(attemptCol - ))
            path += dfs(col, row + 1, possibleSet, distance_row, N)
            possibleSet.add(attemptCol)
    return path

if __name__ == "__main__":
    N = int(input())
    path = 0
    col = []
    distance_row = []
    possibleSet = {i for i in range(N)}

    path += dfs(col, 0, possibleSet, distance_row, N)
    print(path)
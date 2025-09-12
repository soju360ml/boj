import sys
input = sys.stdin.readline
# sys.setrecursionlimit(14)

def dfs(board, checked_x, layer):
    path = 0

    for row in range(1, layer):
        mx = checked_x[row] - (layer - row)
        px = checked_x[row] + (layer - row)
        if 0 < mx:
            board[layer][mx] = 1
        if px < N + 1:
            board[layer][px] = 1

    for i, x in enumerate(board[layer][1:]):
        if x == 1 or checked_x[layer - 1] == i + 1: continue
        else:
            if layer == N:
                board[layer] = [-1 for _ in range(N + 1)]
                return 1
            checked_x[layer] = i + 1
            path += dfs(board, checked_x, layer + 1)
            checked_x[layer] = -1
    board[layer] = [-1 for _ in range(N + 1)]
    checked_x[layer] = -1
    return path
        
if __name__ == "__main__":
    global N
    N = int(input())
    
    path = 0
    for x in range(1, N + 1):
        chessboard = [[-1] * (N + 1) for _ in range(N + 1)]
        chessboard[1][x] = 1
        checked_x = [-1 for _ in range(N + 1)]
        checked_x[x] = x
        layer = 1
        
        path += dfs(chessboard, checked_x, layer + 1)
    print(path)
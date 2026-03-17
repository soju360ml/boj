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

    for i, c in enumerate(board[layer][1:]):
        current_x = i + 1
        flag = 0
        for j in checked_x:
            if current_x == j:
                flag = 1
                break
        if c == 1 or flag == 1: continue
        else:
            if layer == N:
                board[layer] = [-1 for _ in range(N + 1)]
                return 1
            checked_x[layer] = current_x
            path += dfs(board, checked_x, layer + 1)
            checked_x[layer] = -1
    board[layer] = [-1 for _ in range(N + 1)]
    return path
        
if __name__ == "__main__":
    global N
    N = int(input())
    
    path = 0
    for x in range(1, N + 1):
        chessboard = [[-1] * (N + 1) for _ in range(N + 1)]
        checked_x = [-1 for _ in range(N + 1)]
        layer = 1
        checked_x[layer] = x
        
        path += dfs(chessboard, checked_x, layer + 1)
    print(path)
# BOJ 9663
# 비트마스킹으로 퀸의 위치를 체크한다
import sys
input = sys.stdin.readline

def dfs(row, columnX, diagonal1, diagonal2, N):
    path = 0

    for attemptCol in range(N):
        # 아래 세 경우 패스한다
        # 이미 퀸이 놓인 열(columnX)
        # 이미 퀸이 놓인 오른쪽 위 -> 왼쪽 아래 대각선(diagonal1): row + colum 일정
        # 이미 퀸이 놓인 왼쪽 위 -> 오른쪽 아래 대각선(diagonal2): row - colum 일정
        if (
            columnX & 1 << attemptCol or
            diagonal1 & 1 << row + attemptCol or
            diagonal2 & 1 << row - attemptCol + (N - 1)
            ):
            continue

        # 마지막 행인 경우 패스한다
        if row == N - 1:
            path += 1
            continue

        path += dfs(
            row + 1,
            columnX | 1 << attemptCol,
            diagonal1 | 1 << row + attemptCol,
            diagonal2 | 1 << row - attemptCol + (N - 1),
            N
            )
    return path

if __name__ == "__main__":
    N = int(input())
    path = 0

    # 선점한 열
    columnX = 0
    # 선점한 1시 대각선
    diagonal1 = 0
    # 선점한 11시 대각선
    diagonal2 = 0

    path += dfs(0, columnX, diagonal1, diagonal2, N)
    print(path)
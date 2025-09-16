import sys
input = sys.stdin.readline

def dfs(col, row, visitedX, N):
    path = 0

    for attemptCol in range(N):
        # 이미 놓여진 열인 경우 패스
        if attemptCol in visitedX:
            continue

        # 대각선 피하기
        flag = 0
        for i, v in enumerate(col):
            if abs(row - i) == abs(attemptCol - v):
                flag = 1
                break
        if flag == 1: continue

        # 마지막 행으로 넘어가기 전일 경우 선점 가능한 열 확인 후 바로 증가경로 확인
        if row == N - 1:
            path += 1
            continue

        col.append(attemptCol)
        visitedX.add(attemptCol)
        path += dfs(col, row + 1, visitedX, N)
        # 선점한 자리를 다시 복구한 후 다음 열 선점 시도
        visitedX.remove(attemptCol)
        col.pop()
    return path

if __name__ == "__main__":
    N = int(input())
    path = 0
    # 퀸이 놓인 행, 열 => 인덱스, 값
    col = []
    # 이미 선점한 열의 집합
    visitedX = set()

    path += dfs(col, 0, visitedX, N)
    print(path)
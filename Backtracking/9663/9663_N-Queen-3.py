# 이 코드는 백준 9663문제의 최대입력값 14를 입력하면 결과도출까지 35초가 소모된다
# 시간제한 10초를 해결하기 위해 비트마스킹 테크닉 사용하여 코드를 새로 작성해야 한다
import sys
input = sys.stdin.readline

def dfs(row, visitedX, diagonal1, diagonal2, N):
    path = 0

    for attemptCol in range(N):
        # 아래 세 경우 패스한다
        # 이미 퀸이 놓인 열(visitedX)
        # 이미 퀸이 놓인 오른쪽 위 -> 왼쪽 아래 대각선(diagonal1): row + colum 일정
        # 이미 퀸이 놓인 왼쪽 위 -> 오른쪽 아래 대각선(diagonal2): row - colum 일정
        if attemptCol in visitedX or row + attemptCol in diagonal1 or row - attemptCol in diagonal2:
            continue

        # 마지막 행인 경우 패스한다
        if row == N - 1:
            path += 1
            continue

        visitedX.add(attemptCol)
        diagonal1.add(row + attemptCol)
        diagonal2.add(row - attemptCol)
        path += dfs(row + 1, visitedX, diagonal1, diagonal2, N)
        # 선점한 자리 복구
        visitedX.remove(attemptCol)
        diagonal1.remove(row + attemptCol)
        diagonal2.remove(row - attemptCol)
    return path

if __name__ == "__main__":
    N = int(input())
    path = 0

    # 선점한 열
    visitedX = set()
    # 선점한 1시 대각선
    visited_diagonal1 = set()
    # 선점한 11시 대각선
    visited_diagonal2 = set()

    path += dfs(0, visitedX, visited_diagonal1, visited_diagonal2, N)
    print(path)
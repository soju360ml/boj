def is_safe(board, row, col):
    """
    현재 위치 (row, col)에 퀸을 놓을 수 있는지 검사
    """
    # 같은 열에 퀸이 있는지 확인
    for i in range(row):
        if board[i] == col:
            return False

    # 왼쪽 위 대각선에 퀸이 있는지 확인
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i] == j:
            return False
        i -= 1
        j -= 1

    # 오른쪽 위 대각선에 퀸이 있는지 확인
    i, j = row, col
    while i >= 0 and j < len(board):
        if board[i] == j:
            return False
        i -= 1
        j += 1

    return True

def solve_n_queens_util(board, row, n, count):
    """
    백트래킹을 이용해 N-Queen 해법을 찾는 재귀 함수
    """
    # 모든 퀸을 성공적으로 배치했다면 해법 개수 증가
    if row >= n:
        count[0] += 1
        return

    # 현재 행에 퀸을 놓을 수 있는 모든 열을 탐색
    for col in range(n):
        if is_safe(board, row, col):
            # 퀸을 배치
            board[row] = col
            # 다음 행으로 이동
            solve_n_queens_util(board, row + 1, n, count)
            # 백트래킹 (별도의 제거 로직 불필요, board[row]가 덮어쓰여짐)

def solve_n_queens(n):
    """
    N-Queen 문제의 해법 개수를 구하는 메인 함수
    """
    board = [-1] * n  # 각 행에 놓인 퀸의 열 위치를 저장
    count = [0]       # 해법 개수
    solve_n_queens_util(board, 0, n, count)
    return count[0]

# 사용 예시
n = int(input("N을 입력하세요: "))
print(f"N = {n} 일 때 해법의 개수: {solve_n_queens(n)}")
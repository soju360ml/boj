# 지수가 곧 재귀깊이이다. 재귀깊이가 곧 재귀함수의 호출 횟수이다.
# BaseCase는 재귀깊이가 0일 때이다.
# BaseCase에서 출력을 한다.
# 1. '-'를 문자열로 저장한 후 리스트 슬라이싱을 이용해 출력부분을 조절하거나
# 2. 문자열 작성을 하지 않고 재귀단계만으로 출력한다.
# 현재깊이의 분할부분은 지수가 현재깊이-1이다.
# 분할부분의 중간부분은 공백을 출력한다

# 전달인자->재귀깊이
def recur(depth):
    #BaseCase
    if depth == 0:
        print('-', end='')
    #RecursiveCase
    #divisions
    else:
        recur(depth - 1)
        print(' ' * (3 ** (depth - 1)), end='')
        recur(depth - 1)

cases = []
while True:
    try:
        cases.append(int(input()))
    except EOFError:
        break

for i in cases:
    recur(i)
    print()
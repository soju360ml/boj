# 에라토스테네스의 체를 이용해서 특정 구간의 소수테이블을 만들다

# 0부터 n까지의 수 중 소수이면 True, 아니면 False값을 요소로 가지는 테이블을 만든다 + 인덱스가 곧 해당 숫자

# 최대값 입력
n, k = map(int, input().split())
cur_count = 0

if type(n) is int:
    sieve = [True] * (n + 1)
    sieve[0], sieve[1] = False, False

    for i in range(2, n + 1):
        if sieve[i] is True:
            for j in range(i, n + 1, i):
                if sieve[j] is True:
                    cur_count += 1
                    if cur_count == k:
                        print(j)
                    sieve[j] = False
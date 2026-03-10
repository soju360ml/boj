import sys
from collections import defaultdict

# [문제 링크]
# https://www.acmicpc.net/problem/2531

# [문제 정보]
# 분류 : BOJ 2531 : 회전 초밥
# 난이도 : 실버 1

# [풀이 방법]
# 원형 벨트를 구현하기 위해 sushi 리스트를 sushi + sushi[:k-1]로 확장함.
# defaultdict를 사용하여 현재 윈도우에 포함된 초밥 종류와 개수를 실시간 관리함.
# 윈도우가 한 칸 이동할 때마다 양 끝의 초밥 정보만 업데이트하여 O(N)으로 처리함.

input = sys.stdin.readline

def solution():
    n, d, k, c = map(int, input().split())
    check = [0] * (d + 1)
    sushi = []

    for _ in range(n):
        sushi.append(int(input()))
    
    sushi = sushi + sushi[:k]
    result = 0
    count = 0

    for i in range(n):
        # 이전 초밥빼기
        if i > 0:
            check[sushi[i - 1]] = 0
            count -= 1
        for j in range(i, i + k):
            if check[sushi[j]] == 0:
                check[sushi[j]] = 1
                count += 1
        if check[c] == 0:
            result = max(result, count + 1)
        else:
            result = max(result, count)

    print(result)
    return

def clean_solution():
    n, d, k, c = map(int, input().split())
    sushi = []

    for _ in range(n):
        sushi.append(int(input()))
    
    sushi = sushi + sushi[:k]
    check = defaultdict(int)
    check[c] += 1

    for i in range(k):
        check[sushi[i]] += 1

    result = len(check)

    for i in range(n - 1):
        # 이전 초밥빼기
        left = sushi[i]
        check[left] -= 1
        if check[left] == 0:
            del check[left]
        
        # 오른쪽 초밥 추가
        right = sushi[i + k]
        check[right] += 1

        result = max(result, len(check))

    print(result)
    return

if __name__ == "__main__":
    # solution()
    clean_solution()
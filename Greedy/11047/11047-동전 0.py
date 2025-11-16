N, K = map(int, input().split())

value = [int(input()) for _ in range(N)]

count = 0

prev = value[0]
for i in value:
    # print(f'현재 K값은 {K}입니다\ni값은 {i}입니다')
    if K == 0: break
    
    if i == value[-1]:
        remainder = K % i
        count += remainder // prev
        count += K // i
        break

    if K % i == 0:
        prev = i
        continue
    else:
        # print(f'나누어떨어지지 않으므로 나머지연산합니다')
        remainder = K % i
        # print(f'나머지는 {remainder}입니다.\nprev는 {prev}입니다')
        count += remainder // prev
        # print(f'count는 {count}입니다.')
        K -= remainder
        # print(f'K값을 {K}로 수정했습니다.')
        prev = i
        # print('-------------------------')

if N > 1:
    print(count)
else:
    print(K)
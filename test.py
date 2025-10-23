T = int(input())

result = []
for i in range(T):
    H, W, N = map(int, input().split())
    room_number = str((N - 1) // H + 1)
    if len(room_number) == 1:
        room_number = '0' + room_number
    floor = str((N - 1) % H + 1)
    result.append(floor + room_number)

for i in result:
    print(i)
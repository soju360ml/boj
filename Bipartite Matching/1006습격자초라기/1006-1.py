import sys
import copy

count = 0

def list_tuple(dict_1, list_1, cur_max, dict_length):
    global count
    count += 1
    iter_1 = iter(dict_1)
    key_1 = next(iter_1, None)
    count_list_1 = [len(list_1)]

    sum_1 = len(list_1) + dict_length // 2
    if sum_1 <= cur_max:
        return 0

    if key_1:
        for i in dict_1[key_1]:
            if i not in dict_1:
                continue
            list_2 = copy.deepcopy(list_1)
            list_2.append((key_1, i))
            dict_2 = copy.deepcopy(dict_1)
            del dict_2[key_1]
            del dict_2[i]
            count_list_1.append(list_tuple(dict_2, list_2, cur_max, dict_length - 2))
        dict_2 = copy.deepcopy(dict_1)
        del dict_2[key_1]
        count_list_1.append(list_tuple(dict_2, list_1, cur_max, dict_length - 1))
        cur_max = max(count_list_1)
    return max(count_list_1)

T = int(sys.stdin.readline())
result_list_1 = []

for a in range(T):
    N, W = map(int, sys.stdin.readline().split())
    line_1 = [int(x) for x in sys.stdin.readline().split()]
    line_2 = [int(x) for x in sys.stdin.readline().split()]
    line_1.extend(line_2)

    dict_1 = {}
    for i in range(1, N * 2 + 1):
        near_set = []
        if N > 1:
            if i % N == 1:
                near_set.append((i + N - 1, line_1[i + N - 2]))
                near_set.append((i + 1, line_1[i]))
            elif i % N != 1 and i % N != 0:
                near_set.append((i - 1, line_1[i - 2]))
                near_set.append((i + 1, line_1[i]))
            elif i % N == 0:
                near_set.append((i - N + 1, line_1[i - N]))
                near_set.append((i - 1, line_1[i - 2]))
            
            if i // (N + 1) == 0:
                near_set.append((i + N, line_1[i + N - 1]))
            elif i // (N + 1) == 1:
                near_set.append((i - N, line_1[i - N - 1]))

            for near, count in near_set:
                if line_1[i - 1] + count <= W:
                    if i not in dict_1:
                        dict_1[i] = [near]
                    else:
                        dict_1[i].append(near)
        
        if N == 1 and line_1[0] + line_2[0] <= W:
            dict_1[1] = [2]
            dict_1[2] = [1]

    for i, value in dict_1.items():
        dict_1[i].sort()

    dict_len_1 = 0
    for key, value in dict_1.items():
        dict_len_1 += len(value)

    result_1 = list_tuple(dict_1, [], 0, dict_len_1)
    result_list_1.append(N * 2 - result_1)

for i in range(len(result_list_1)):
    print(result_list_1[i])
print(count)
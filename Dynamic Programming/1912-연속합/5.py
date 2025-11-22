N = int(input())
seq = list(map(int, input().split()))

for i in range(1, N):
    seq[i] = seq[i - 1] + seq[i] if seq[i] + seq[i - 1] > seq[i] else seq[i]

print(max(seq))
a = int(input())
b = int(input())
c = int(input())
k = a * b * c
s = str(k)
for i in range(10):
    print(s.count(str(i)))
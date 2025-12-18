import timeit
import random

data = [random.random() for _ in range(1000000)]

# sorted() 측정
t_sorted = timeit.timeit(lambda: sorted(data), number=1)

# .sort() 측정
t_sort = timeit.timeit(lambda: data.sort(), number=1)

print(f"sorted(): {t_sorted:.5f}초")
print(f".sort(): {t_sort:.5f}초")
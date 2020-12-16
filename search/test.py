# test binary search vs linear search for sorted array.
import binary_search, linear_search
import math
import time

a = [1, 2, 3]
print(binary_search.search(a, 1.5))
# start = time.time()
# for i in range(1, 100):
#     a = list(range(i))
#     key = int(i/10)
#     binary_search.search(a, key)
# end = time.time()
# print(end - start)

# start = time.time()
# for i in range(100, 10000):
#     a = list(range(i))
#     key = int(i/10)
#     linear_search.search(a, key)
# end = time.time()
# print(end-start)
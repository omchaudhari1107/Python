# Maintain cache
# it is a technique which is used to improve the performance of a program by stroing the result of funmction call so
# that you can reuse the result
from functools import lru_cache
import time


@lru_cache(maxsize=None)  # Least Recently Used
def fx(n):
    time.sleep(5)
    return n * 5


print(fx(20))
print("done for 20")
print(fx(2))
print("done for 20")

print(fx(20))
print("done for 20")
print(fx(2))
print("done for 20")

# 100
# done for 20
# 10
# done for 20 from here the output is directly printed
# 100
# done for 20
# 10
# done for 20

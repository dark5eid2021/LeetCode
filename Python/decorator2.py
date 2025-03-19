from functools import lru_cache

@lru_cache
def increment(num):
    print('Running 1000 lines of code')
    return num+1



print(increment(1))
print(increment(2))
print(increment(3))
print(increment(1))
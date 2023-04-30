from functools import lru_cache

N, MOD = int(input()), 998244353

@lru_cache(maxsize=None)
def f(n):
    if n > N:
        return 0
    if n == N:
        return 1
    return sum(f(i * n) for i in range(2, 7)) * pow(5, MOD - 2, MOD) % MOD

print(f(1))

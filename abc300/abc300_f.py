N, M, K = map(int, input().split())
S = input()
lo, hi = K, N * M + 1
while lo + 1 < hi:
    mi = (lo + hi) // 2
    x = S.count('x') * (mi // N) + S[: mi % N].count('x')
    ok = False
    for i in range(N):
        ok |= x <= K
        if mi + i >= N * M:
            break
        x += S[(mi + i) % N] == 'x'
        x -= S[i] == 'x'
    if ok:
        lo = mi
    else:
        hi = mi
print(lo)

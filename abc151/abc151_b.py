import math

n, k, m = map(int, input().split())
a = list(map(int, input().split()))

sum_a = sum(a)
target_sum = m * n

if target_sum - sum_a > k:
    print("-1")
else:
    min_score = max(0, target_sum - sum_a)
    print(min_score)

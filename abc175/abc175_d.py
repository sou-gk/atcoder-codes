n, k = map(int, input().split())
c = list(map(int, input().split()))
p = list(map(int, input().split()))

score = 0
max_score = 0
visited = [False] * n

for i in range(n):
    if visited[i]:
        continue
    visited[i] = True
    j = p[i]
    cycle = [c[j - 1]]
    while j != i + 1:
        visited[j - 1] = True
        cycle.append(c[j - 1])
        j = p[j - 1]
    cycle_len = len(cycle)
    cumsum = [0] * (cycle_len + 1)
    for l in range(cycle_len):
        cumsum[l + 1] = cumsum[l] + cycle[l]
    for l in range(1, cycle_len + 1):
        if l > k:
            break
        s = cumsum[l] + max(0, cumsum[cycle_len] - cumsum[cycle_len - l])
        max_score = max(max_score, s)

print(max_score)

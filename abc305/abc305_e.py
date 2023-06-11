from collections import deque

n, m, k = map(int, input().split())
p = list(map(int, input().split()))
h = list(map(int, input().split()))
g = [[] for _ in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    g[a-1].append(b-1)
    g[b-1].append(a-1)

# 各頂点を警備できる警備員の集合を求める
V = [[] for _ in range(n)]
for i in range(k):
    q = deque([(p[i]-1, 0)])
    visited = [False] * n
    visited[p[i]-1] = True
    while q:
        v, d = q.popleft()
        if d > h[i]:
            break
        V[v].append(i)
        for u in g[v]:
            if not visited[u]:
                visited[u] = True
                q.append((u, d+1))

# 警備されている頂点を小さい方から順に列挙する
S = set()
ans = []
while len(S) < n:
    v = None
    for u in range(n):
        if u not in S and all(i in V[u] for i in S):
            v = u
            break
    if v is None:
        print(-1)
        exit()
    ans.append(v+1)
    S.add(v)
    for i in range(k):
        if i not in V[v]:
            continue
        q = deque([(p[i]-1, 0)])
        visited = [False] * n
        visited[p[i]-1] = True
        while q:
            u, d = q.popleft()
            if d > h[i]:
                break
            if u != v:
                V[u].remove(i)
            for w in g[u]:
                if not visited[w]:
                    visited[w] = True
                    q.append((w, d+1))

print(*ans)

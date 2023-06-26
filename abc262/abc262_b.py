from collections import deque

def count_triplets(n, edges):
    # グラフを隣接リスト形式で表現
    graph = [[] for _ in range(n+1)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    # aからbへのパスを全列挙し、その中からcに向かうパスを見つける
    count = 0
    for a in range(1, n+1):
        for b in graph[a]:
            if b <= a:
                continue
            visited = [False] * (n+1)
            visited[a] = True
            q = deque([(b, False)])
            while q:
                v, has_c = q.popleft()
                if v == a:
                    if has_c:
                        count += 1
                    break
                for u in graph[v]:
                    if not visited[u]:
                        visited[u] = True
                        q.append((u, has_c or u == c))
    return count

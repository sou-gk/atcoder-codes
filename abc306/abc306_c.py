N = int(input())
A = list(map(int, input().split()))

f = {}
for i in range(N):
    f[i+1] = []

for j in range(3*N):
    f[A[j]].append(j)

ans = []
for i in range(1, N+1):
    ans.append(f[i][1])

ans.sort()
print(*[i+1 for i in ans])

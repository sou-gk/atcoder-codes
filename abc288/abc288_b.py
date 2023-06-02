n, k = map(int, input().split())
s = []
for i in range(n):
    si = input()
    s.append(si)

s.sort()  # 辞書順にソート

for i in range(k):
    print(s[i])

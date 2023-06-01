n = int(input())
l = list(map(int, input().split()))

l.sort()  # 長さを昇順にソート

count = 0
for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            if l[i] != l[j] and l[j] != l[k] and l[k] != l[i]:  # 長さが異なる場合
                if l[i] + l[j] > l[k]:  # 三角形を作ることができる場合
                    count += 1

print(count)

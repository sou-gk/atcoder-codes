n = int(input())
a = list(map(int, input().split()))

a.sort()
s = [0] * n

for i in range(0, n, 2):
    s[i] = a[i // 2]

for i in range(1, n, 2):
    s[i] = a[-(i // 2 + 1)]

if all(s[i-1] < s[i] > s[i+1] if 0 < i < n-1 else True for i in range(n)):
    print("Yes")
else:
    print("No")

n, m = map(int, input().split())
p = [0] * n
s = [""] * n

for i in range(m):
    pi, si = input().split()
    pi = int(pi) - 1
    if si == "AC":
        p[pi] = 1
    elif p[pi] == 0:
        s[pi] += "WA"

ac_count = sum(p)
wa_count = sum(len(si) for i, si in enumerate(s) if p[i] == 1)

print(ac_count, wa_count)

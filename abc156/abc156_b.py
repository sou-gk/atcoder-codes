n, k = map(int, input().split())
digits = 0
while n > 0:
    n //= k
    digits += 1
print(digits)

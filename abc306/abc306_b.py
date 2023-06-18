A = list(map(int, input().split()))

decimal = 0
for i in range(64):
    decimal += A[i] * (2 ** i)

print(decimal)

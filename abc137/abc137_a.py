A, B = map(int, input().split())

add = A + B
sub = A - B
mul = A * B

print(max(add, sub, mul))

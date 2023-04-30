H, W = map(int, input().split())
A = [input() for _ in range(H)]
B = [input() for _ in range(H)]

def shift_left(C):
    return [r[1:] + r[0] for r in C]

def shift_up(C):
    return C[1:] + [C[0]]

ans = False
for i in range(H):
    for j in range(W):
        ans |= A == B
        A = shift_left(A)
    A = shift_up(A)
print('Yes' if ans else 'No')

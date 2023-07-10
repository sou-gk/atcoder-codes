def can_represent(N, K):
    digits = []
    while N > 0:
        digits.append(N % 3)
        N //= 3
    
    if K > len(digits):
        return "No"
    
    for i in range(K):
        if digits[i] != 0:
            return "No"
    
    return "Yes"

T = int(input())  # テストケースの数

for _ in range(T):
    N, K = map(int, input().split())
    result = can_represent(N, K)
    print(result)

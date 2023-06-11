points = [0, 3, 4, 8, 9, 14, 23]

p, q = input().split()

p_idx = ord(p) - ord('A')
q_idx = ord(q) - ord('A')

distance = abs(points[p_idx] - points[q_idx])

print(distance)

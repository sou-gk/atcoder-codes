n = int(input())  
nearest = 0  
min_distance = float('inf')  

for i in range(22):
    p = i * 5  
    d = abs(n - p)  
    if d < min_distance:  
        min_distance = d
        nearest = p

print(nearest)  

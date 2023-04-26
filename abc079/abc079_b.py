N = int(input())

L=[]

for i in range(N+1):
    if i == 0:
        L.append(2)
    elif i == 1:
        L.append(1)
    else:
        L.append(L[i-1] + L[i-2])

print(L[N])

N=input()

n0 = N[0]
n1 = N[1]
n2 = N[2]
n3 = N[3]

if n0 == n1 and n0 == n2:
    print("Yes")
elif n1 == n2 and n1 == n3:
    print("Yes")
else:
    print("No")

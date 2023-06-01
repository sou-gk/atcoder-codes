s = input()

max_rainy_days = 0
current_rainy_days = 0

for i in range(3):
    if s[i] == "R":
        current_rainy_days += 1
        max_rainy_days = max(max_rainy_days, current_rainy_days)
    else:
        current_rainy_days = 0

print(max_rainy_days)

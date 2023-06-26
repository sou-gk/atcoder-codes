y = int(input())
current_year = y

next_year = current_year
while (next_year % 4 != 2):
    next_year += 1

print(next_year)

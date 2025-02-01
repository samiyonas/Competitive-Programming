year = int(input())

for years in range(year + 1, 9001):
    digits = set(str(years))
    if len(digits) == 4:
        print(years)
        break
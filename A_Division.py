testcases = int(input())
divs = []

for _ in range(testcases):
    divs.append(int(input()))

for i in divs:
    if i >= 1900:
        print("Division 1")
    elif 1600 <= i and i <= 1899:
        print("Division 2")
    elif 1400 <= i and i <= 1599:
        print("Division 3")
    else:
        print("Division 4")
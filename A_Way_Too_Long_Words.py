n = int(input())
words = []

for _ in range(n):
    words.append(input())

for i in words:
    if len(i) > 10:
        num = len(i) - 2
        print(i[0] + str(num) + i[len(i) - 1])
    else:
        print(i)
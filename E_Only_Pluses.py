testcases = int(input())
arr = []
for i in range(testcases):
    arr.append(map(int, input().split(" ")))

counter = 0
for i in arr:
    abc = sorted(i)
    for j in range(2):
        
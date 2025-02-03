n = int(input())
problems = []

for _ in range(n):
    problems.append(list(map(int, input().split(" "))))

problemsSolved = 0
for i in problems:
    counter = 0
    for j in range(len(i)):
        if i[j] == 1:
            counter += 1
    if counter >= 2:
        problemsSolved += 1

print(problemsSolved)
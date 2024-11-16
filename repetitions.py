dna = input()

i = 0
j = 0
Max = 1

while i < len(dna) - 1:
    if dna[i] != dna[i + 1]:
        j = i + 1
    else:
        Max = max(Max, i - j + 2)
    i += 1
print(Max)
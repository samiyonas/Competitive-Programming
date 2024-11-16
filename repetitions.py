"""
You are given a DNA sequence: a string consisting of characters A, C, G, and T. Your task is to find the longest repetition in the sequence. This is a maximum-length substring containing only one type of character.

Input
The only input line contains a string of n characters.

Output
Print one integer: the length of the longest repetition.

Constraints
1 <= n <= 10**6

Example
Input:
ATTCGGGA

Output:
3
"""

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
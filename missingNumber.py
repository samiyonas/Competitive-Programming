"""
You are given all numbers between 1,2,...,n except one. Your task is to find the missing number.

Input
The first input line contains an integer n.
The second line contains n-1 numbers. Each number is distinct and between 1 and n (inclusive).

Output
Print the missing number.

Constraints
2 <= n <= 2.10**5

Example

Input:
5
2 3 1 5

Output:
4
"""
n = int(input())

numbers = input().split(" ")
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])
numbers.sort()
for number in range(len(numbers)):
    if number + 1 != numbers[number]:
        print(number + 1)
        break
    if number + 1 == len(numbers):
        print(n)
        break

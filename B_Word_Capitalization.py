string = input()

if string[0].isupper():
    print(string)
else:
    print(string[0].capitalize() + string[1:])
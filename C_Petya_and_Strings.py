first_str = input()
second_str = input()

if first_str.lower() == second_str.lower():
    print(0)
elif first_str.lower() > second_str.lower():
    print(1)
else:
    print(-1)
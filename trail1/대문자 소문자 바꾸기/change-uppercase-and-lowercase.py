s = input()

for i in s:
    if 'a' <= i <= 'z':
        print(i.upper(), end="")
    else:
        print(i.lower(), end="")

        
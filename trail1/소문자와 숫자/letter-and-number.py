s = list(input())

for i in s:
    if i.isalpha():
        print(i.lower(), end="")
    elif '0' <= i <= '9':
        print(i, end="")
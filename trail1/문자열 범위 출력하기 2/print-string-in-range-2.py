string = input()
n = int(input())

if n >= len(string):
    print(string[::-1])

else:
    for j in string[:len(string)-1-n:-1]:
        print(j, end="")
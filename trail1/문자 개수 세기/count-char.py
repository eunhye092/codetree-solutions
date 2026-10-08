string = input()
a = input()

num = 0

for i in range(len(string)):
    if string[i] == a:
        num += 1

print(num)
a = input()
sum = 0

for i in a:
    if '0' <= i <= '9':
        i = int(i)
        sum += i

print(sum)
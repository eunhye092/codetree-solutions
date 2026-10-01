n = int(input())

for i in range(n):
    for j in range(n):
        num = 11 + 2 * (i + j)
        print(num, end=" ")
    print()
n = int(input())
sum = 0

for i in range(n):
    for j in range(n):
        if i % 2 == 0:
            sum += 1
            print(sum, end=" ")
        else:
            sum += 2
            print(sum, end=" ")
    print()

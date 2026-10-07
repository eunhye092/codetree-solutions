n = int(input())

for i in range(1, n+1):
    sum = i
    for j in range(1, n+1):
        print(sum, end=" ")
        sum += n
    print()
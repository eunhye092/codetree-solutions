sum = 0

for i in range(4):
    a = list(map(int, input().split()))

    for j in range(4):
        if j <= i:
            sum += a[j]

print(sum)

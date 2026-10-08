n = int(input())

a =[
    [1 for _ in range(i+1)]
    for i in range(n)
]

for i in range(n):
    for j in range(i):
        if j  != 0:
            a[i][j] = a[i-1][j-1] + a[i-1][j]

for row in a:
    for elem in row:
        print(elem, end=" ")
    print()
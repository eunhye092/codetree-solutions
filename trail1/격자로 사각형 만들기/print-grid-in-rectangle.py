n = int(input())

a = [
    [0 for _ in range(n)]
    for _ in range(n)
]

for i in range(n):
    a[i][0] = 1
    a[0][i] = 1

for i in range(1, n):
    for j in range(1, n):
        a[i][j] = a[i-1][j] + a[i][j-1] + a[i-1][j-1]

for row in a:
    for elem in row:
        print(elem, end=" ")
    print()
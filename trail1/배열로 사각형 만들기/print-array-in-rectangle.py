a = [
    [0 for _ in range(5)]
    for _ in range(5)
]

for i in range(5):
    a[i][0] = 1
    a[0][i] = 1

for i in range(1, 5):
    for j in range(1, 5):
        a[i][j] = a[i-1][j] + a[i][j-1]

for row in a:
    for elem in row:
        print(elem, end=" ")
    print()
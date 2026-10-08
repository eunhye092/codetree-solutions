n, m = tuple(map(int, input().split()))

arr = [
    [0 for _ in range(n)]
    for _ in range(n)
]

for _ in range(m):
    r, c = tuple(map(int, input().split()))

    for i in range(n):
        for j in range(n):
            if i + 1 == r and j + 1 == c:
                arr[r-1][c-1] = (i + 1) * (j + 1)

for row in arr:
    for elem in row:
        print(elem, end=" ")
    print()
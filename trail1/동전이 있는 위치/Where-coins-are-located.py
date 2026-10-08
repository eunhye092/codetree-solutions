n, m = map(int, input().split())

arr = [
    [0 for _ in range(n)]
    for _ in range(n)
]

for _ in range(m):
    r, c = tuple(map(int, input().split()))

    for i in range(1, n+1):
        for j in range(1, n+1):
            arr[r-1][c-1] = 1

for row in arr:
    for elem in row:
        print(elem, end=" ")
    print()
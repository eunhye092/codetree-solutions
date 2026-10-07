n, m = map(int, input().split())

# Please write your code here.
start = 0

arr = [
    [0 for _ in range(m)]
    for _ in range(n)
]

for j in range(m):
    for i in range(n):
        if j % 2 == 0:
            arr[i][j] = start
        else:
            arr[n-i-1][j] = start
        start += 1

for row in arr:
    for elem in row:
        print(elem, end=" ")
    print()
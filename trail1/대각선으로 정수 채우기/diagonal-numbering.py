n, m = map(int, input().split())

# Please write your code here.
arr = [
    [0 for _ in range(m)]
    for _ in range(n)
]

num = 1

for k in range(n+m-1):
    for i in range(n):
        for j in range(m):
                if k == i + j:
                    arr[i][j] = num
                    num += 1


for row in arr:
    for elem in row:
        print(elem, end=" ")
    print()
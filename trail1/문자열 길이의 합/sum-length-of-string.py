n = int(input())

arr = [
    input()
    for _ in range(n)
]

cnt, sum = 0, 0

for i in arr:
    sum += len(i)
    if i[0] == 'a':
        cnt += 1

print(sum, cnt)
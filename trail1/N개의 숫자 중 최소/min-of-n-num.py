n = int(input())
arr = list(map(int, input().split()))
min = arr[0]
cnt = 0

for i in arr[1::]:
    if i < min:
        min = i
for j in arr:
    if j == min:
        cnt += 1

print(min, cnt)
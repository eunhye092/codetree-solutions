arr = list(map(int, input().split()))
max = arr[0]
min = arr[0]

for i in arr:
    if i == 999 or i == -999:
        break

    if i > max:
        max = i
    elif i < min:
        min = i


print(max, min)
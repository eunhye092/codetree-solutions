count = [0] * 5

for _ in range(3):
    arr = input().split()
    x = str(arr[0])
    y = int(arr[1])

    if x == 'Y' and y >= 37:
        count[1] += 1
    elif x =='N' and y >= 37:
        count[2] += 1
    elif x == 'Y' and y < 37:
        count[3] += 1
    elif x == 'N' and y < 37:
        count[4] += 1

for i in count[1:5]:
    print(i, end=" ")

if count[1] >= 2:
    print('E')
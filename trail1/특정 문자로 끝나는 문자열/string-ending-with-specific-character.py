arr = [
    input()
    for _ in range(11)
]

cnt = 0

for i in arr[:10:]:
    if i[len(i)-1] == arr[10]:
        print(i)
        cnt += 1

if cnt == 0:
    print("None")
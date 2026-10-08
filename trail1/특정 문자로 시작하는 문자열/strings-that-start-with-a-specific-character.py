n = int(input())

arr = [
    input()
    for _ in range(n)
]

string = input()

cnt, sum = 0, 0

for i in range(n):
    if arr[i][0] == string:
        cnt += 1
        sum += len(arr[i])

average = sum / cnt

print(f"{cnt} {average:.2f}")
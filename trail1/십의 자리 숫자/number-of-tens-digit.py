arr = list(map(int, input().split()))
count = [0] * 10

for i in arr:
    if i == 0:
        break
    elif i >= 10:
        i //= 10
        count[i] += 1

for i in range(1, 10):
    print(f"{i} - {count[i]}")
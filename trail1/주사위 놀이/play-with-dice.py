arr = list(map(int, input().split()))
count = [0] * 7

for elem in arr:
    count[elem] += 1

for i in range(1, 7):
    print(f"{i} - {count[i]}")
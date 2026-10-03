inputs = list(map(int, input().split()))
arr = []

for i in inputs:
    if i % 3 == 0:
        break
    else:
        arr.append(i)

print(arr[-1])        
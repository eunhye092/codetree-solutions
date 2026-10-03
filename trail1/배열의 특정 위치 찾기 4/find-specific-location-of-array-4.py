inputs = list(map(int, input().split()))
arr =[]

for i in inputs:
    if i == 0:
        break
    elif i % 2 == 0:
        arr.append(i)

print(len(arr), sum(arr))
inputs = list(map(int, input().split()))
arr = []

for i in inputs:
    if i == 0:
        break
    
    arr.append(i)

    if len(arr) == 10:
        break

for i in arr[::-1]:
    print(i, end=" ")
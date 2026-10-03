inputs = list(map(int, input().split()))
arr =[]

for i in inputs:
    if i == 0:
        break
    arr.append(i)
    if len(arr) == 10:
        break

print(f"{sum(arr)} {sum(arr)/len(arr):.1f}")
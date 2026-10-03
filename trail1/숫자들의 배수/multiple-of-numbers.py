n = int(input())
arr = [n]

for i in range(1, 10):
    
    if n == 10:
        arr.append(20)
        break
    elif n == 5:
        arr.append(10)
        break

    arr.append(arr[i-1]+n)

    if arr[i-1] // 10 == n:
        break

for elem in arr:
    print(elem, end=" ")
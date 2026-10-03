arr = list(map(int, input().split()))
new_arr =[]

for i in range(100):
    if arr[i] == 0:
        break
    elif arr[i] % 2 == 0:
        new_arr.append(arr[i]//2)
    elif arr[i] % 2 == 1:
        new_arr.append(arr[i]+3)
   

for i in new_arr:
    print(i, end=" ")
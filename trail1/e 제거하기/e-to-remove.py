s = input()
arr = list(s)

for i in range(len(s)-1):
    if arr[i] == 'e':
        arr.pop(i)
        s = ''.join(arr)
        print(s)
        break


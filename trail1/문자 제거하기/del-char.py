s = input()
arr = list(s)

for i in range(len(arr)-1):
    n = int(input())

    if n >= len(arr):
        arr.pop(len(arr)-1)
    else:
        arr.pop(n)

    s = ''.join(arr)
    print(s)

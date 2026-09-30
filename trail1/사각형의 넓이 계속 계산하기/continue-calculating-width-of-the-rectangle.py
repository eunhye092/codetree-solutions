while True:
    arr = input().split()
    h = int(arr[0])
    v = int(arr[1])
    s = str(arr[2])

    if s != 'C':
        print(h*v)
        continue
    print(h*v)
    break
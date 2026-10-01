a, b = map(int, input().split())
cnt = (b - a) // 2 + 1

for i in range(1, 10):
    for j in range(0, cnt):
        print(f"{b-2*j} * {i} = {(b-2*j)*i}", end=" ")
        if j < cnt - 1:
            print("/", end=" ")
    print()
    
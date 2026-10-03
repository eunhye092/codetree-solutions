n = int(input())

for _ in range(n):
    i = int(input())
    cnt = 0
    while i != 1:
        if i % 2 == 0:
            i //= 2
        else:
            i = 3 * i + 1
        cnt += 1
    print(cnt)
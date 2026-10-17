a = input()
b = input()

cnt = 0

for i in range(1, len(a)):
    a = a[-1] + a[:-1]
    cnt += 1

    if a == b:
        print(cnt)
        break

    elif i == len(a)-1 and a != b:
        print(-1)

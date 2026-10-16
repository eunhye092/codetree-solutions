a, b = map(int,input().split())

sum = str(a + b)
cnt = 0

for i in sum:
    if i == '1':
        cnt += 1

print(cnt)
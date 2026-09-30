a, b, c = map(int, input().split())
sat = False
cnt = 0

for i in range(a, b+1):
    if i % c == 0:
        cnt += 1

if cnt == 0:
    sat = True

if sat == True:
    print("YES")
else:
    print("NO")
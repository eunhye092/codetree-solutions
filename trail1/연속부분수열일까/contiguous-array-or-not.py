cnt_a, cnt_b = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
idx = -1
for i in range(cnt_a-cnt_b+1):
    if b == a[i:cnt_b+i]:
        idx = 1

if idx == 1:
    print('Yes')
else:
    print("No")
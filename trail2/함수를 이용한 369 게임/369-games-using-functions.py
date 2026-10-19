a, b = map(int, input().split())

# Please write your code here.
def check_369(n):
    return ('3' in str(n)) or ('6' in str(n)) or ('9' in str(n))

def check_3(n):
    return n % 3 == 0

cnt = 0
for i in range(a, b+1):
    if check_369(i) or check_3(i):
        cnt += 1

print(cnt)
n, m = map(int, input().split())

# Please write your code here.

def LCM(n, m):
    i = max(n,m)
    while i >= max(n, m):
        if i % n == 0 and i % m == 0:
            lcm = i
            break
        i += 1
    print(lcm)

LCM(n, m)
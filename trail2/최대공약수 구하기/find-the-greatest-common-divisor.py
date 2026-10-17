n, m = map(int, input().split())

# Please write your code here.

def GCD(n,m):
    for i in range(1, 101):
        if n % i == 0 and m % i == 0:
            gcd = i
        if i == max(n,m):
            break
    print(gcd)

GCD(n,m)
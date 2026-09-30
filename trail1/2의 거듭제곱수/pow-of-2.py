n = int(input())
x = 0

while True:
    
    if n % 2 == 0:
        x += 1
        n = n // 2
    elif n == 1:
        print(x)
        break 
n = int(input())
i = 1

while i >= 1:
    a = n // i
    
    if a > 1:
        n = a
        i += 1
        continue
    else:
        print(i)
        break
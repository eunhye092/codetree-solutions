a, b = map(int, input().split())

# Please write your code here.

def prime_number(a, b):
    pnl = []
    for i in range(a, b+1):
        is_pn = True
        for j in range(2, i):
            if i % j == 0:
                is_pn = False
                break
        if is_pn:
            pnl.append(i)
    
    return pnl

def even_digit_cnt(a, b, n):
    cnt = 0
    for i in n:
        if (i // 10 + i % 10) % 2 == 0:
            cnt += 1
    return cnt

print(even_digit_cnt(a, b, prime_number(a, b)))
n, m = map(int, input().split())
A = list(map(int, input().split()))

# Please write your code here.
sum = 0
def add(m, A):
    global sum
    sum += A[m-1]

def cal_m(m, A):
    while m >= 1:
        add(m, A)
        if m == 1:
            break
        if m % 2 == 0:
            m //= 2
        else:
            m -= 1
    
cal_m(m, A)
print(sum)
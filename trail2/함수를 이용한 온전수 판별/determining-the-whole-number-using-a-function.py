a, b = map(int, input().split())

# Please write your code here.

def clean_number_count(a, b):
    cnt = 0
    for i in range(a, b+1):
        is_cn = True

        if (i % 2 == 0) or (i % 10 == 5) or (i % 3 == 0 and i % 9 != 0):
            is_cn = False
        
        if is_cn == True:
            cnt += 1
    
    return cnt

print(clean_number_count(a, b))
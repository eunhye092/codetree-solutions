a, b = map(int, input().split())

# Please write your code here.

def cal(a, b):
    if a > b:
        a += 25
        b *= 2
        print(a, b)
    else:
        a *= 2
        b += 25
        print(a, b)

cal(a, b)
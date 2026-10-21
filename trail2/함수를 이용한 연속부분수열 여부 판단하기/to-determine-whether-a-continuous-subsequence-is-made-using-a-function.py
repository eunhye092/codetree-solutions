n1, n2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Please write your code here.
def con_sub(a, b):
    for i in range(len(a)):
        if a[i:len(b)+i] == b:
            return True
    return False

if con_sub(a, b):
    print("Yes")
else:
    print("No")
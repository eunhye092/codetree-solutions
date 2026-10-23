a, b = map(int, input().split())

# Please write your code here.
def operation(a, b):
    if a > b:
        a *= 2
        b += 10
        return a, b
    else:
        a += 10
        b *= 2
        return a, b

operation(a, b)

for i in operation(a, b):
    print(i, end=" ")
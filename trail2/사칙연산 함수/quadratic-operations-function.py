a, o, c = input().split()
a = int(a)
c = int(c)

# Please write your code here.
def add(a, o, c):
    return f"{a} {o} {c} = {a+c}"

def sub(a, o, c):
    return f"{a} {o} {c} = {a-c}"

def mul(a, o, c):
    return f"{a} {o} {c} = {a*c}"

def div(a, o, c):
    return f"{a} {o} {c} = {a//c}"

if o == '+':
    print(add(a, o, c))

elif o == '-':
    print(sub(a, o, c))

elif o == '*':
    print(mul(a, o, c))

elif o == '/':
    print(div(a, o, c))

else:
    print('False')
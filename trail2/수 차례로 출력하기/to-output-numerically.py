n = int(input())

# Please write your code here.
def print_num(n):

    for i in range(n):
        print(i+1, end=" ")
    return
    
def print_num1(n):
    for i in range(n):
        print(n-i, end=" ")
    return
print_num(n)
print()
print_num1(n)
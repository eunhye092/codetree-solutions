N = int(input())

# Please write your code here.
def factorial(N):
    if N == 0 or N == 1:
        return 1
    
    return factorial(N-1) * N

print(factorial(N)) 
a, b = map(int, input().split())

# Please write your code here.

def find_prime_sum(a, b):
    is_prime = True
    sum = 0
    for i in range(a, b+1):
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break
            else:
                is_prime = True

        if is_prime == True:
            sum += i
    return sum

print(find_prime_sum(a, b))



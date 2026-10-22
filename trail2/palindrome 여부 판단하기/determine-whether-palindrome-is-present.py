A = input()

# Please write your code here.

def palindrome(A):
    for i in range(len(A)):
        if A == A[::-1]:
            return True
    return False

if palindrome(A):
    print("Yes")
else:
    print("No")
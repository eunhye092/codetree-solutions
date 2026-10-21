M, D = map(int, input().split())

# Please write your code here.

def is_date_2021(M, D):
    if M == 2 and D <= 28:
        return True
    elif M <= 12 and M != 2 and D <= 30:
        return True
    elif (M == 1 or M == 3 or M == 5 or M == 7 or M == 8 or M == 10 or M == 12) and D == 31:
        return True
    else:
        return False

if is_date_2021(M, D):
    print("Yes")
else:
    print("No")
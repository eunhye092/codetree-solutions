n = int(input())

for i in range(n):
    for j in range(n):
        if i == 0:
            print("*", end=" ")
        elif i % 2 == 1:
            if (j > i and j % 2 == 1) or i == j:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        else:
            if j > i and j % 2 == 1: 
                print("*", end=" ")
            else:
                print(" ", end=" ")
            
    print()
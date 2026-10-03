n, q = map(int, input().split())
arr = list(map(int, input().split()))

for _ in range(q):
    question = list(map(int, input().split()))

    if question[0] == 1:
        print(arr[question[1]-1], end="")
    
    elif question[0] == 2:
        for i in range(n):
            if arr[i] == question[1]:
                print(i+1, end="")
                break
            elif arr.count(question[1]) == 0:
                print(0, end="")
                break
    
    elif question[0] == 3:
        for i in arr[question[1]-1:question[2]]:
            print(i, end=" ")

    print()
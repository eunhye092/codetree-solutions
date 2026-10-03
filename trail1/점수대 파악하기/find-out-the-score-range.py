arr = list(map(int, input().split()))
count = [0] * 11

for elem in arr:
    if elem == 0:
        break
    count[elem//10] += 1

for i in range(10,0,-1):
    print(f"{i*10} - {count[i]}")
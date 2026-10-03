arr = list(map(int, input().split()))
cnt = 0
sum = 0

for i in arr[::]:
    if i >= 250:
        break  
    else:
        sum += i
        cnt += 1

print(sum, f"{sum/cnt:.1f}")
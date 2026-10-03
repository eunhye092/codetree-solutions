arr = list(map(int, input().split()))

sum_even = 0
sum = 0
cnt = 0

for i in arr[1::2]:
    sum_even += i

for i in arr[2::3]:
    sum += i
    cnt += 1

print(f"{sum_even} {sum/cnt:.1f}")
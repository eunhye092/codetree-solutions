cnt = 0
sum = 0

while True:
    a = int(input())

    if 20 <= a < 30:
        cnt += 1
        sum += a
        continue
    break

print(f"{sum/cnt:.2f}")
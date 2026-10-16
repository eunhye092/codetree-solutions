n = int(input())
sum = 0

for _ in range(n):
    s = int(input())

    sum += s

sum = str(sum)

print(sum[1:]+sum[:1])
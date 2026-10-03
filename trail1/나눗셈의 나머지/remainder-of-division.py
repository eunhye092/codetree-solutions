a, b = map(int, input().split())
count = [0] * 10
sum = 0

while a > 1:
    r = a % b
    a //= b
    count[r] += 1

for i in range(10):
    sum += count[i] ** 2

print(sum)
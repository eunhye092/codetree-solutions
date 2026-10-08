arr = ["apple", "banana", "grape", "blueberry", "orange"]

letter = input()

num = 0

for i in arr:
    for j in range(2, 4):
        if i[j] == letter or i[j] == letter:
            print(i)
            num += 1

print(num)
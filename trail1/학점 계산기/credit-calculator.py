n = int(input())
arr = list(map(float, input().split()))

ans = sum(arr)

average = ans / n
print(f"{average:.1f}")

if average >= 4:
    print("Perfect")
elif average >= 3:
    print("Good")
else:
    print("Poor")


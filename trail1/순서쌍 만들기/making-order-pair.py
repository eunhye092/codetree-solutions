n = int(input())

for i in range(n):
    for j in range(n):
        a, b = n-i, n-j
        print(f"({a},{b})", end=" ")
    print()
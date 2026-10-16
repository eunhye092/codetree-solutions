a, b = tuple(input().split())
A = []
B = []

for i in a:
    if '0' <= i <= '9':
        A.append(i)
    else:
        break

for i in b:
    if '0' <= i <= '9':
        B.append(i)
    else:
        break

A = int(''.join(A))
B = int(''.join(B))

print(A+B)

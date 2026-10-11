str = list(input())
s = str[1]

for i in range(len(str)):
    if str[i] == s:
        str[i] = str[0]

str = ''.join(str)
print(str)
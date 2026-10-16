str1 = input()
str2 = input()

s1 = ''
s2 = ''

for i in str1:
    if '0' <= i <= '9':
        s1 += i

for i in str2:
    if '0' <= i <= '9':
        s2 += i

s1 = int(s1)
s2 = int(s2)

print(s1+s2)
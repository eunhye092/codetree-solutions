s = input()
o = list(input())

for i in o:
    if i == 'R':
        s = s[-1] + s[:-1]
    else:
        s = s[1:] + s[0]

print(s)
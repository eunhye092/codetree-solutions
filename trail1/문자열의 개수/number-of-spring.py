cnt = 0
string =[]

for i in range(200):
    str = input()

    if str == '0':
        break
    
    if i % 2 == 0:
        string.append(str)

    cnt += 1

print(cnt)

for i in string:
    print(i)
n = input()
num1 = 0
num2 = 0

for i in range(len(n)):
    if n[i:i+2] == 'ee':
        num1 += 1
    elif n[i:i+2] == 'eb':
        num2 += 1

print(num1, num2)
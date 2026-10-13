s = input()

for i in range(len(s)):
    string = s[len(s)-i:] + s[:len(s)-i]
    print(string)

print(s)
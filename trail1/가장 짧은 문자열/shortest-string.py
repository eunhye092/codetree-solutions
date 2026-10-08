str1 = input()
str2 = input()
str3 = input()

len1 = len(str1)
len2 = len(str2)
len3 = len(str3)

len = [len1, len2, len3]

print(max(len)-min(len))
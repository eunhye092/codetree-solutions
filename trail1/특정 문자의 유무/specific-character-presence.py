n = input()
existee = False
existab = False

for i in range(len(n)):
    if n[i:i+2] == "ee":
        existee = True
    if n[i:i+2] == "ab":
        existab = True

if existee == True:
    print("Yes", end=" ")
else:
    print("No", end=" ")

if existab == True:
    print("Yes")
else:
    print("No")    
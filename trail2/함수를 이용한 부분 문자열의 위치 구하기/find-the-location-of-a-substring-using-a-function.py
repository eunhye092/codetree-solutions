text = input()
pattern = input()

# Please write your code here.
def is_pattern(text, pattern):
        if pattern in text:
            return True
        else:
            return False

def find_position(text, pattern):
    if is_pattern(text, pattern):
        for i in range(len(text) - len(pattern) + 1):
            if pattern == text[i:i+len(pattern)]:
                return print(i)
    else:
        print(-1)

find_position(text, pattern)
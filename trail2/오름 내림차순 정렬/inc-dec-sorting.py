n = int(input())
nums = list(map(int, input().split()))

# Please write your code here.

for i in range(n):
    nums.sort()
    print(nums[i], end=" ")

print()

for i in range(n):
    nums.sort(reverse=True)
    print(nums[i], end=" ")
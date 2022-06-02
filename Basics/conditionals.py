# For loop
nums = [1, 2, 3, 4, 5]

for i in range(5):
    print(nums[i])

for num in nums:
    print(num)

for index, num in enumerate(nums):
    print(index, num)


# While loop
index = 0
while index < len(nums):
    print(nums[index])
    index += 1

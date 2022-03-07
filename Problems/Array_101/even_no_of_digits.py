"""
Given an array nums of integers, return how many of them contain an even number of digits.
"""

def find_numbers(nums):
    result = 0
    for i in range(0, len(nums)):
        count = len(str(nums[i]))
        if count % 2 == 0:
            result += 1
    return result


def main():
    nums = [23, 1245, 124]
    result = find_numbers(nums)
    print(f"Even no of digits: {result}")


if __name__ == '__main__':
    main()

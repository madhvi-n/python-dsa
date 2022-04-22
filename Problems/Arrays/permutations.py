from functools import reduce


def permute(nums):
    return [[n] + p
            for i, n in enumerate(nums)
            for p in permute(nums[:i] + nums[i + 1:])] or [[]]


def permute_2(nums):
    return nums and [p[:i] + [nums[0]] + p[i:]
                     for p in permute_2(nums[1:])
                     for i in range(len(nums))] or [[]]


def permute_3(nums):
    return reduce(lambda x, n: [p[:i] + [n] + p[i:]
                                for p in x for i in range(len(p) + 1)],
                  nums, [[]])


def permutations(nums: list) -> list:
    result = []

    if len(nums) == 1:
        return [nums[:]]

    for i in range(len(nums)):
        num = nums.pop()
        perms = permutations(nums)

        for perm in perms:
            perm.append(num)
        result.extend(perms)
        nums.append(num)
    return result


def main():
    print(permutations([1, 2, 3]))


if __name__ == '__main__':
    main()

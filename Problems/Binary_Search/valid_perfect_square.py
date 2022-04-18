"""
https://leetcode.com/problems/valid-perfect-square/
Given a positive integer num, write a function which returns True if num is a perfect square else False.

Follow up: Do not use any built-in library function such as sqrt.
"""


def perfect_square(num: int) -> bool:
    start = 0
    end = num

    while start <= end:
        # Find mid
        mid = start + (end - start) // 2

        square = mid * mid

        # If mid * mid == num, return True
        if square == num:
            return True

        # If square is greater than num, square lies in the LHS side
        if square > num:
            end = mid - 1
        else:
            start = mid + 1

    return False


def main():
    print(perfect_square(16))
    print(perfect_square(14))
    print(perfect_square(25))
    print(perfect_square(100))
    print(perfect_square(200))


if __name__ == '__main__':
    main()

"""
https://leetcode.com/problems/guess-number-higher-or-lower/

We are playing the Guess Game. The game is as follows:
I pick a number from 1 to n. You have to guess which number I picked.
Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.
You call a pre-defined API int guess(int num), which returns three possible results:

-1: Your guess is higher than the number I picked (i.e. num > pick).
1: Your guess is lower than the number I picked (i.e. num < pick).
0: your guess is equal to the number I picked (i.e. num == pick).
Return the number that I picked.
"""


def guess(num: int, pick:int):
    if num > pick:
        return -1
    elif num < pick:
        return 1
    else:
        return 0


def guess_number(n: int, pick: int) -> int:
    start = 0
    end = n

    while start <= end:
        mid = start + (end - start) // 2

        res = guess(n, pick)

        if res == 1:
            start = mid + 1
        elif res == -1:
            end = mid - 1
        else:
            return mid


def main():
    print(guess_number(10, 6))


if __name__ == '__main__':
    main()

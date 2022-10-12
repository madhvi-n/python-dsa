from typing import List

"""
Time complexity: O(4^n)
Space: Same
"""


def add_operators(num: str, target: int) -> List[str]:
    def backtracking(index=0, path="", value=0, prev=None):
        if index == len(num) and value == target:
            result.append(path)
            return

        for i in range(index + 1, len(num) + 1):
            tmp = int(num[index: i])
            if i == index + 1 or (i > index + 1 and num[index] != ""):
                if prev is None:
                    backtracking(i, num[index: i], tmp, tmp)
                else:
                    backtracking(i, path + '+' + num[index: i], value + tmp, tmp)
                    backtracking(i, path + '-' + num[index: i], value - tmp, -tmp)
                    backtracking(i, path + '*' + num[index: i], value - prev + prev * tmp, prev * tmp)

    result = []
    backtracking()
    return result


def add_operators_2(expression: str, target: int) -> list:
    def backtrack(i, path, diff, prev_num):
        if i == len(expression):
            if diff == target:
                ans.append(path)
            return

        for j in range(i, len(expression)):
            if j > i and expression[i] == '0':
                break  # Skip leading zero number

            num = int(expression[i:j + 1])
            if i == 0:
                backtrack(j + 1, path + str(num), diff + num,
                          num)  # First num, pick it without adding any operator
            else:
                backtrack(j + 1, path + "+" + str(num), diff + num, num)
                backtrack(j + 1, path + "-" + str(num), diff - num, -num)
                backtrack(j + 1, path + "*" + str(num), diff - prev_num + prev_num * num,
                          prev_num * num)  # Can imagine with example: 1+2*3*4

    ans = []
    backtrack(0, "", 0, 0)
    return ans


def main():
    pass


if __name__ == '__main__':
    main()

"""
Given n pairs of parentheses, write a function to generate all combinations of
well-formed parentheses.

Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
"""


def generate_parenthesis(n: int) -> list[str]:
    # keep track of opened and closed parentheses added till now
    # add open parentheses if open_count < n, call dfs for open_count + 1 and pop the parentheses
    # add closed parentheses if closed_count < open_count, call dfs for closed_count + 1 and pop the parentheses
    # if open_count == closed_count == n, we've one parenthesis combination

    stack = []
    result = []

    def backtrack(open_count, closed_count):
        if open_count == closed_count == n:
            result.append("".join(stack))
            return

        if open_count < n:
            stack.append("(")
            backtrack(open_count + 1, closed_count)
            stack.pop()

        if closed_count < open_count:
            stack.append(")")
            backtrack(open_count, closed_count + 1)
            stack.pop()

    backtrack(0, 0)
    return result


def main():
    print(generate_parenthesis(3))
    print(generate_parenthesis(4))
    print(generate_parenthesis(5))


if __name__ == '__main__':
    main()
from typing import List


def evaluate_rpn(tokens: List[str]) -> int:
    stack = []

    for token in tokens:
        if token in "+-*/":
            left, right = stack.pop(), stack.pop()
            if token == "+":
                val = right + left
            elif token == "-":
                val = right - left
            elif token == "*":
                val = right * left
            else:
                val = right / left
            stack.append(int(val))
        else:
            stack.append(int(token))
    return stack[-1]


def eval_rpn(tokens: List[str]) -> int:
    operator_map = {
        "+": lambda l, r: l + r,
        "*": lambda l, r: l * r,
        "-": lambda l, r: l - r,
        "/": lambda l, r: int(l / r),
    }

    stack = []
    for token in tokens:
        if token in operator_map:
            right = stack.pop()
            left = stack.pop()
            token = operator_map[token](left, right)
        stack.append(int(token))

    return stack.pop()


def evaluate(tokens: List[str]) -> int:
    stack = []
    for c in tokens:
        if c not in ['+', '-', '*', '/']:
            stack.append(int(c))
        else:
            a = stack.pop()
            b = stack.pop()
            if c == '+':
                c = b + a
            elif c == '-':
                c = b - a
            elif c == '*':
                c = b * a
            elif c == '/':
                c = int(b / a)
            stack.append(c)

    return stack[0]


def main():
    print(eval_rpn(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))
    print(evaluate_rpn(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))
    print(evaluate(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))


if __name__ == '__main__':
    main()

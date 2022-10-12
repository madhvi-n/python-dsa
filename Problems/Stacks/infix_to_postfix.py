"""
Steps:
Create an empty stack called operator_stack for keeping operators. Create an empty list for output.

Convert the input infix string to a list by using the string method split.

Scan the token list from left to right.

If the token is an operand, append it to the end of the output list.

If the token is a left parenthesis, push it on the operator_stack.

If the token is a right parenthesis, pop the operator_stack until the corresponding left parenthesis is removed. Append each operator to the end of the output list.

If the token is an operator, *, /, +, or -, push it on the operator_stack. However, first remove any operators already on the operator_stack that have higher or equal precedence and append them to the output list.

When the input expression has been completely processed, check the operator_stack. Any operators still on the stack can be removed and appended to the end of the output list.
"""


def infix_to_postfix(infix_expr):
    precedence = {"*": 3, "/": 3, "+": 2, "-": 2, "(": 1}
    operator_stack = []
    postfix_list = []
    token_list = infix_expr.split()

    for token in token_list:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfix_list.append(token)
        elif token == "(":
            operator_stack.append(token)
        elif token == ")":
            top_token = operator_stack.pop()
            while top_token != "(":
                postfix_list.append(top_token)
                top_token = operator_stack.pop()
        else:
            while operator_stack and \
                    (precedence[operator_stack[-1]] >= precedence[token]):
                postfix_list.append(operator_stack.pop())
            operator_stack.append(token)

    while operator_stack:
        postfix_list.append(operator_stack.pop())
    return " ".join(postfix_list)


def main():
    print(infix_to_postfix("A * B + C * D"))
    print(infix_to_postfix("( A + B ) * C - ( D - E ) * ( F + G )"))


if __name__ == '__main__':
    main()

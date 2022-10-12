"""
Convert infix expression to prefix expression
"""


def infix_to_prefix(expression: str) -> str:
    pass


def main():
    infix_to_prefix("(A+B)*(C+D)*(E+F)")
    infix_to_prefix("A+((B+C)*(D+E))")
    infix_to_prefix("A*B*C*D+E+F")


if __name__ == '__main__':
    main()

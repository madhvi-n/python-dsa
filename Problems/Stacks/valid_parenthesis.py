def valid(s: str):
    stack = []
    close_to_open = {")": "(", "]": "[", "}": "{"}

    for bracket in s:
        if bracket in close_to_open:
            if stack and stack[-1] == close_to_open[bracket]:
                stack.pop()
            else:
                return False
        else:
            stack.append(bracket)
    return True if not stack else False


def main():
    print(valid("()(){}["))
    print(valid("{()(){}}"))


if __name__ == "__main__":
    main()

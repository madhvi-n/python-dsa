def reverse(s: str):
    stack = []

    for char in s:
        stack.append(char)

    res = ""
    for char in stack:
        res = char + res

    return res


def reverse_string(s: str):
    stack = []

    for char in s:
        stack.append(char)

    res = ""
    index = len(stack)
    while index > 0:
        res += stack[index - 1]
        index -= 1

    return res


def main():
    print(reverse("leetcode"))
    print(reverse_string("leetcode"))


if __name__ == "__main__":
    main()

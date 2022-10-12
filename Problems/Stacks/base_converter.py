
def base_converter(decimal_num, base):
    digits = "0123456789ABCDEF"
    stack = []

    while decimal_num > 0:
        remainder = decimal_num % base
        stack.append(remainder)
        decimal_num = decimal_num // base

    result = ""
    while stack:
        result += digits[stack.pop()]
    return result


def main():
    print(base_converter(25, 2))
    print(base_converter(256, 16))
    print(base_converter(26, 26))


if __name__ == '__main__':
    main()

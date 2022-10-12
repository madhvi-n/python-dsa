"""
https://leetcode.com/problems/check-if-a-parentheses-string-can-be-valid/

A parentheses string is a non-empty string consisting only of '(' and ')'.
It is valid if any of the following conditions is true:
    It is ().
    It can be written as AB (A concatenated with B), where A and B are valid parentheses strings.
    It can be written as (A), where A is a valid parentheses string.


You are given a parentheses string s and a string locked, both of length n.
locked is a binary string consisting only of '0's and '1's. For each index i of locked,
    If locked[i] is '1', you cannot change s[i].
    But if locked[i] is '0', you can change s[i] to either '(' or ')'.

Return true if you can make s a valid parentheses string. Otherwise, return false.

Input: s = "))()))", locked = "010100"
Output: true
Explanation: locked[1] == '1' and locked[3] == '1', so we cannot change s[1] or s[3].
We change s[0] and s[4] to '(' while leaving s[2] and s[5] unchanged to make s valid.
"""


def valid(s: str, locked: str):
    if len(s) % 2 == 1:
        return False

    total = open_count = closed_count = 0
    for i in range(len(s) - 1, -1, -1):
        if locked[i] == '0':
            total += 1
        elif s[i] == '(':
            open_count += 1
        elif s[i] == ')':
            closed_count += 1
        if total - open_count + closed_count < 0:
            return False

    total = open_count = closed_count = 0
    for i in range(len(s)):
        if locked[i] == '0':
            total += 1
        elif s[i] == '(':
            open_count += 1
        elif s[i] == ')':
            closed_count += 1
        if total + open_count - closed_count < 0:
            return False
    return True


def main():
    print(valid(s="()()", locked="0000"))
    print(valid(s=")", locked="0"))


if __name__ == "__main__":
    main()

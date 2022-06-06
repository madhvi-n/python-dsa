"""
Given a set of strings, return them in lexicographic order (dictionary/alphabetical order).

Input: [code, coder, coding, coded, codex, codify, codependents, codes, codesign, codeveloper]
Output: [code, coded, codependents, coder, codes, codesign, codeveloper, codex, codify, coding]
"""


class TrieNode:
    def __init__(self):
        self.children = dict.fromkeys(list('abcdefghijklmnopqrstuvwxyz'), None)
        self.word_end = None


def insert(root, word):
    curr = root
    for char in word:
        if curr.children[char] is None:
            curr.children[char] = TrieNode()
        curr = curr.children[char]
    curr.word_end = word


def lex_sorting(words: list[str]) -> list[str]:
    head = TrieNode()

    for word in words:
        insert(head, word)

    result = []

    def dfs(root, result):
        if root is None:
            return

        if root.word_end:
            result.append(root.word_end)

        for key, child in root.children.items():
            dfs(child, result)

    dfs(head, result)
    return result


def main():
    words = [
        'code', 'coder', 'coding', 'coded', 'codex', 'codify',
        'codependents', 'codes', 'codesign', 'codeveloper'
    ]
    print(lex_sorting(words))


if __name__ == '__main__':
    main()

"""
Given a set of strings, find their longest common prefix (LCP).

Input: ['technique', 'technician', 'technology', 'technical']
Output: 'techn'

Input: ['techie delight', 'tech', 'techie', 'technology', 'technical']
Output: 'tech'
"""


class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False


def insert(root, word):
    curr = root
    for char in word:
        curr = curr.children.setdefault(char, TrieNode())
    curr.end_of_word = True


def longest_common_prefix(words: list) -> str:
    head = TrieNode()

    for word in words:
        insert(head, word)

    lcp = ""
    curr = head

    # loop until we find the end of word and node has only 1 child
    while curr and not curr.end_of_word and len(curr.children) == 1:
        for key, val in curr.children.items():
            lcp += key
            curr = val
    return lcp


def main():
    words = [
        'code', 'coder', 'coding', 'codable', 'codec', 'codecs', 'coded',
        'codeless', 'codependence', 'codependency', 'codependent',
        'codependents', 'codes', 'codesign', 'codesigned', 'codeveloped',
        'codeveloper', 'codex', 'codify', 'codiscovered', 'codrive'
    ]
    print(f"longest common prefix is: {longest_common_prefix(words)}")


if __name__ == '__main__':
    main()

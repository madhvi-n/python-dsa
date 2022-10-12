"""
Given a string s, return the number of distinct non-empty substrings.

Constraints:
0 ≤ n ≤ 1,000 where n is the length of s
Example 1
Input
s = "aaab"
Output
7
"""


class TrieNode:
    def __init__(self, character=None):
        self.children = {}
        self.word_end = False
        self.character = character


class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.node_count = 0

    def insert(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode(char)
                self.node_count += 1
            curr = curr.children[char]
        curr.word_end = True


def distinct_substrings(string: str) -> int:
    t = Trie()

    for index in range(0, len(string)):
        t.insert(string[index:])

    return t.node_count


def main():
    print(distinct_substrings("aaab"))
    print(distinct_substrings("abc"))
    print(distinct_substrings("xyzzy"))


if __name__ == '__main__':
    main()

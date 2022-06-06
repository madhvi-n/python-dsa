"""
Given an array of strings words representing an English Dictionary, return the longest word in words that can
be built one character at a time by other words in words.

If there is more than one possible answer, return the longest word with the smallest lexicographical order.
If there is no answer, return the empty string.

Constraints:
1 <= words.length <= 1000
1 <= words[i].length <= 30
words[i] consists of lowercase English letters.

Example 1:
Input: words = ["w","wo","wor","worl","world"]
Output: "world"
Explanation: The word "world" can be built one character at a time by "w", "wo", "wor", and "worl".
"""
from collections import deque


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


def longest_word(words: list[str]) -> str:
    head = TrieNode()
    result = []
    for word in words:
        insert(head, word)

    def dfs(root):
        for key, child in root.children.items():
            if child and child.word_end:
                if len(child.word_end) > len(result):
                    result.append(child.word_end)
                dfs(child)

    dfs(head)
    print(result)
    return result[-1] if result else ""


# Another solution using Trie
class TNode:
    def __init__(self):
        self.children = {}
        self.word = None
        self.word_end = False


class Trie:
    def __init__(self):
        self.root = TNode()

    def insert(self, word):
        curr = self.root
        for char in word:
            curr = curr.children.setdefault(char, TNode())
        curr.word = word
        curr.word_end = True

    def bfs(self):
        queue = deque([self.root])
        res = ''
        while queue:
            curr = queue.popleft()
            for child in curr.children.values():
                if child.word_end:
                    queue.append(child)
                    if len(child.word) > len(res) or child.word < res:
                        res = child.word
        return res


def longest_word_ii(words: list[str]) -> str:
    trie = Trie()
    for word in words:
        trie.insert(word)
    return trie.bfs()


def main():
    print(longest_word(['w', 'wo', 'wor', 'worl', 'world']))
    # print(longest_word_ii(["a", "banana", "app", "appl", "ap", "apply", "apple"]))


if __name__ == '__main__':
    main()

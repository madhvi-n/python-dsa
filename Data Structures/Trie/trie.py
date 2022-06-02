"""
Trie or Prefix tree
"""


class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            # if char not in curr.children, create new TrieNode
            # else set curr equal to that children

            # if char not in curr.children:
            #     curr.children[char] = TrieNode()
            # curr = curr.children[char]
            curr.children.setdefault(char, TrieNode())
        curr.end_of_word = True

    def search(self, word: str) -> bool:
        curr = self.root
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return curr.end_of_word

    def starts_with(self, prefix: str) -> bool:
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return True


def main():
    trie = Trie()
    trie.insert("apple")
    print(trie.search("apple"))
    print(trie.search("app"))
    print(trie.starts_with("ap"))


if __name__ == '__main__':
    main()

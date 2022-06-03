"""
Trie or Prefix tree
"""


class TrieNode:
    def __init__(self):
        self.children = {}
        self.prefix_count = 0
        self.word_end = 0


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            curr = curr.children.setdefault(char, TrieNode())
            curr.prefix_count += 1
        curr.word_end += 1

    def count_words_equal_to(self, word: str) -> int:
        curr = self.root
        for char in word:
            if char not in curr.children:
                return 0
            curr = curr.children[char]
        return curr.word_end

    def count_words_starting_with(self, prefix: str) -> int:
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return 0
            curr = curr.children[char]
        return curr.prefix_count

    def erase(self, word: str) -> bool:
        curr = self.root
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        if curr.word_end > 0:
            curr.word_end -= 1
            return True
        return False


def main():
    trie = Trie()
    trie.insert("apple")
    trie.insert("app")
    trie.insert("ape")
    trie.insert("bat")
    trie.insert("bag")
    trie.insert("blue")
    trie.insert("blue")
    print(["apple", "app","ape", "bat", "bag", "blue", "blue"])
    print("Count word starting with ap: ", trie.count_words_starting_with("ap"))
    print("Count word starting with b: ", trie.count_words_starting_with("b"))
    print("Count word starting with app: ", trie.count_words_starting_with("app"))
    print("Count word equal to app: ", trie.count_words_equal_to("app"))
    print("Count word equal to blue: ", trie.count_words_equal_to("blue"))
    trie.erase("blue")
    print("Count word equal to blue: ", trie.count_words_equal_to("blue"))


if __name__ == '__main__':
    main()

"""
Design a special dictionary with some words that searchs the words in it by a prefix and a suffix.

Implement the WordFilter class:
WordFilter(string[] words) Initializes the object with the words in the dictionary.
f(string prefix, string suffix) Returns the index of the word in the dictionary,
which has the prefix and the suffix.
If there is more than one valid index, return the largest of them.
If there is no such word in the dictionary, return -1.

Example 1:
Input
["WordFilter", "f"]
[[["apple"]], ["a", "e"]]
Output
[null, 0]

Explanation:
wordFilter = new WordFilter(["apple"]);
wordFilter.f("a", "e"); // return 0, because the word at index 0 has prefix = "a" and suffix = 'e".
"""


class TrieNode:
    def __init__(self):
        self.children = {}
        self.index = 0
        self.word_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word, index):
        curr = self.root
        for char in word:
            curr = curr.children.setdefault(char, TrieNode())
        curr.index = index
        curr.word_end = True

    def starts_with(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                return -1
            curr = curr.children[char]
        return curr.index


class WordFilter:
    def __init__(self, words):
        self.trie = Trie()

        for index, word in enumerate(words):
            new_word = word + '#' + word
            for i in range(len(word)):
                self.trie.insert(long[i:], index)

    def f(self, prefix, suffix):
        return self.trie.starts_with(prefix + '#' + suffix)


"""
Let n be number of words, L be maximum length of word. One of the cool ways to solve this problem is the following: 
imagine, we have word apple, then what we need to find is substring suffix + # + prefix in string apple#apple. 
Now, quick way to find substring is for example create Trie with all suffixes of apple#apple, which include #.

It is O(nL^2) time and space for init:
for each word we need O(L^2) processing time. 
For f we need O(L) time and O(1) space, because we just traverse through tree. 
So, final complexity is O(nL^2 + QL), where Q is number of queries.
"""


def main():
    words = [
        "cabaabaaaa", "ccbcababac", "bacaabccba", "bcbbcbacaa", "abcaccbcaa",
        "accabaccaa", "cabcbbbcca", "ababccabcb", "caccbbcbab", "bccbacbcba"
    ]
    word_filter = WordFilter(words)
    print(word_filter.f(["ab", "abcaccbcaa"]))
    print(word_filter.f(["a", "aa"]))
    print(word_filter.f(["cabaaba", "abaaaa"]))
    print(word_filter.f(["cacc", "accbbcbab"]))
    print(word_filter.f(["ccbcab", "bac"]))
    print(word_filter.f(["bac", "cba"]))
    print(word_filter.f(["ac", "accabaccaa"]))
    print(word_filter.f(["bcbb", "aa"]))
    print(word_filter.f(["ccbca", "cbcababac"]))


if __name__ == '__main__':
    main()

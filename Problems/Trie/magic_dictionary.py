from collections import Counter
from typing import List


class MagicDictionary:

    def __init__(self):
        self.words = None
        self.near = dict()

    @staticmethod
    def candidates(word: str):
        for i in range(len(word)):
            yield word[:i] + '*' + word[i + 1:]

    def build_dict(self, dictionary: List[str]) -> None:
        self.words = set(dictionary)
        self.near = Counter(cand for word in self.words for cand in self.candidates(word))

    def search(self, word: str) -> bool:
        return any(self.near[cand] > 1 or
                   self.near[cand] == 1 and word not in self.words
                   for cand in self.candidates(word))


def main():
    d = MagicDictionary()
    d.build_dict(["hello", "leetcode"])
    print(d.search("hello"))
    print(d.search("hhllo"))
    print(d.search("hell"))
    print(d.search("leetcoded"))


if __name__ == '__main__':
    main()

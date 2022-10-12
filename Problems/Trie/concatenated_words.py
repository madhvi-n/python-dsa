"""
Given an array of strings words (without duplicates), return all the concatenated words in the given list of words.
A concatenated word is defined as a string that is comprised entirely of at least two shorter words in the given array.

Example 1:

Input: words = [
    "cat", "cats", "catsdogcats", "dog", "dogcatsdog", "hippopotamuses", "rat", "ratcatdogcat"
]
Output: ["catsdogcats", "dogcatsdog", "ratcatdogcat"]

Explanation:
    - "catsdogcats" can be concatenated by "cats", "dog" and "cats";
    - "dogcatsdog" can be concatenated by "dog", "cats" and "dog";
    - "ratcatdogcat" can be concatenated by "rat", "cat", "dog" and "cat".
"""


def find_all_concatenated_words_in_dict(words: list[str]) -> list[str]:
    dictionary = set(words)

    def dfs(word):
        for i in range(1, len(word)):
            prefix = word[:i]
            suffix = word[i:]

            if prefix in dictionary and suffix in dictionary:
                return True

            if prefix in dictionary and dfs(suffix):
                return True

            if suffix in dictionary and dfs(prefix):
                return True

        return False

    res = []
    for word in words:
        if dfs(word):
            res.append(word)
    return res


def find_concatenated_words(words: list[str]) -> list[str]:
    dictionary = set(words)
    memo = {}

    def dfs(word):
        if word in memo:
            return memo[word]

        memo[word] = True
        
        for i in range(1, len(word)):
            prefix = word[:i]
            suffix = word[i:]
            if prefix in dictionary and suffix in dictionary:
                memo[word] = True
                break
            if prefix in dictionary and dfs(suffix):
                memo[word] = True
                break
            if suffix in dictionary and dfs(prefix):
                memo[word] = True
                break
        return memo[word]
    return [word for word in words if dfs(word)]

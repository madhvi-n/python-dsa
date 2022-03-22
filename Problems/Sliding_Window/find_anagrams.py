"""
https://leetcode.com/problems/find-all-anagrams-in-a-string/

Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
"""
from typing import List


def findAnagrams(string: str, pattern: str) -> List[int]:

    if len(pattern) > len(string):
        return []

    pCount, sCount = dict(), dict()

    # Building hashmap for pattern and string limited to pattern length
    for i in range(len(pattern)):
        pCount[pattern[i]] = 1 + pCount.get(pattern[i], 0)
        sCount[string[i]] = 1 + sCount.get(string[i], 0)

    # If both dicts are equal, then pattern starts at index 0 hence append 0 in the result else []
    res = [0] if pCount == sCount else []

    # Initiate left pointer to maintain sliding window of length = len(pattern)
    left = 0

    #Build hashmap for remaining length of string
    # Remove character at left index from string as you move forward, maintaining the window
    for i in range(len(pattern), len(string)):
        sCount[string[i]] = 1 + sCount.get(string[i], 0)
        sCount[string[left]] -= 1

        #Pop the string character if the count is 0
        if sCount[string[left]] == 0:
            sCount.pop(string[left])

        #Incrementing the left pointer by 1
        left += 1

        #If both dicts are equal, pattern started at left index
        if sCount == pCount:
            res.append(left)
    return res


def main():
    print(findAnagrams("cbaebabacd", "abc"))
    print(findAnagrams("abab", "ab"))


if __name__ == '__main__':
    main()

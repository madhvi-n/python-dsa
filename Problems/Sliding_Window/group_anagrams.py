"""
https://leetcode.com/problems/group-anagrams/

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
"""
from typing import List
from collections import defaultdict

def group_anagrams(strs: List[str]) -> List[str]:
    #Naive method
    #Sorting and comparing each string in list
    #For loop, O(m * n logn)

    hashMap = dict()
    for word in strs:
        sortedword = "".join(sorted(word))
        if sortedword not in hashMap:
            hashMap[sortedword] = [word]
        else:
            hashMap[sortedword].append(word)

    result = []
    for value in hashMap.values():
        result.append(value)
    return result

#O (m * n) => m = len of list and n is length of word
def group_anagrams_2(strs: List[str]) -> List[str]:
    res = defaultdict(list)
    for s in strs:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord("a")] += 1
    
        res[tuple(count)].append(s)
    return list(res.values())


def main():
    res = group_anagrams(["eat","tea","tan","ate","nat","bat"])
    print(res)

if __name__ == '__main__':
    main()

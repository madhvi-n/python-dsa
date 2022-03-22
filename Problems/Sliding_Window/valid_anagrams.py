"""
https://leetcode.com/problems/valid-anagram/

Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

"""


def isAnagram(s: str, t: str) -> bool:
    #Length of unequal strings cannot be anagram
    if len(s) != len(t):
        return False

    hashMap = dict()
    #Add count of characters into hashMap for one string and remove count for another
    #If count is greater than 0 for any string, not an anagram

    for character in s:
        hashMap[character] = 1 + hashMap.get(character, 0)

    for character in t:
        if character in hashMap:
            hashMap[character] -= 1

    for count in hashMap.values():
        if count > 0:
            return False
    return True


def main():
    print(isAnagram("anagram","nagaram"))
    print(isAnagram("rat", "car"))

if __name__ == '__main__':
    main()

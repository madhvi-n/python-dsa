"""
You are given a list of strings words from the alien language's dictionary, where the strings in words are sorted lexicographically by the rules of the new language.

Given a sorted dictionary (array of words) of an alien language, find order of characters in the language.
Return a string of the unique letters in the new alien language sorted lexicographically increasing order
by the new language's rules. If there is no solution, return "". If there are multiple solutions, return any of them

Input:  words[] = ['baa', 'abcd', 'abca', 'cab', 'cad']
Output: 'bdac'

Input:  words = ['wrt', 'wrf', 'er', 'ett', 'rftt']
Output: 'wertf'

Input:  words[] = ['caa', 'aaa', 'aab']
Output: 'cab'
"""
from collections import defaultdict


# Topological sort
def alien_dictionary(words: list[list[str]]) -> str:
    adjacency_list = {char: set() for word in words for char in word}

    for i in range(len(words) - 1):
        w1, w2 = words[i], words[i+1]
        min_length = min(len(w1), len(w2))

        if len(w1) > len(w2) and w1[:min_length] == w2[:min_length]:
            return ""

        for j in range(min_length):
            if w1[j] != w2[j]:
                adjacency_list[w1[j]].add(w2[j])
                break

    visited = dict()
    result = []

    def dfs(char):
        if char in visited:
            return visited[char]

        visited[char] = True
        for adjacent in adjacency_list[char]:
            if dfs(adjacent):
                return True

        visited[char] = False
        result.append(char)

    for c in adjacency_list:
        if dfs(c):
            return ""
    result.reverse()
    return "".join(result)


def main():
    print(alien_dictionary(['wrt', 'wrf', 'er', 'ett', 'rftt']))
    print(alien_dictionary(['baa', 'abcd', 'abca', 'cab', 'cad']))


if __name__ == '__main__':
    main()

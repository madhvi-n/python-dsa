"""
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words
beginWord -> s1 -> s2 -> ... -> sk such that:
Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return all the shortest transformation sequences
from beginWord to endWord, or an empty list if no such sequence exists. Each sequence should be returned as a list of
the words [beginWord, s1, s2, ..., sk].

Example 1:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]
Explanation: There are 2 shortest transformation sequences:
"hit" -> "hot" -> "dot" -> "dog" -> "cog"
"hit" -> "hot" -> "lot" -> "log" -> "cog"
Example 2:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: []
Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.
"""
from collections import defaultdict, deque


# Using BFS
def word_ladder(begin_word: str, end_word: str, words: list[str]) -> list[list]:
    if end_word not in words or not end_word or not begin_word or not words or begin_word == end_word:
        return []

    length = len(begin_word)

    # Dictionary to hold combination of words that can be formed,
    # from any given word. By changing one letter at a time
    dictionary = defaultdict(list)
    for word in words:
        for i in range(length):
            dictionary[word[:i] + "*" + word[i + 1:]].append(word)

    queue = deque([(begin_word, [begin_word])])
    visited = set([begin_word])
    result = []

    while queue and not result:
        q_length = len(queue)
        level_discovered = set()

        for _ in range(q_length):
            word, path = queue.popleft()

            for i in range(length):
                pattern = word[:i] + "*" + word[i+1:]
                for next_word in dictionary[pattern]:
                    if next_word == end_word:
                        result.append(path + [end_word])

                    if next_word not in level_discovered:
                        level_discovered.add(next_word)
                        queue.append((next_word, path + [next_word]))
        visited = visited.union(level_discovered)
    return result


# Using BFS to build adjacency list and DFS to find shortest path
def word_ladder_ii(begin_word: str, end_word: str, words: list[str]):
    if end_word not in words or not end_word or not begin_word or not words or begin_word == end_word:
        return []

    length = len(begin_word)

    # Dictionary to hold combination of words that can be formed,
    # from any given word. By changing one letter at a time
    dictionary = defaultdict(list)
    for word in words:
        for i in range(length):
            dictionary[word[:i] + "*" + word[i + 1:]].append(word)
    depth = 0
    found = False
    parents = defaultdict(list)
    queue = deque([begin_word])
    visited = set([begin_word])

    while queue and not found:
        depth += 1
        q_length = len(queue)
        level_discovered = set()
        for _ in range(q_length):
            word = queue.popleft()
            for i in range(length):
                pattern = word[:i] + "*" + word[i+1:]
                for next_word in dictionary[pattern]:
                    if next_word == end_word:
                        continue

                    if next_word not in visited:
                        parents[next_word].append(word)
                        if next_word == end_word:
                            found = True
                        visited.add(next_word)
                        queue.append(next_word)
                        
        visited = visited.union(level_discovered)

    result = []

    def dfs(node, path, depth):
        if depth == 0:
            if path[-1] == begin_word:
                result.append(path[::-1])
            return

        for parent in parents[node]:
            path.append(parent)
            dfs(parent, path, depth - 1)
            path.pop()

    dfs(end_word, [end_word], depth)
    return result


def main():
    print(word_ladder("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
    print(word_ladder("hot", "dog", ["hot", "cog", "dog", "tot", "hog", "hop", "pot", "dot"]))
    print(word_ladder("a", "c", ["a", "b", "c"]))


if __name__ == '__main__':
    main()

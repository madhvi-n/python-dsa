"""
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words
beginWord -> s1 -> s2 -> ... -> sk such that:
    - Every adjacent pair of words differs by a single letter.
    - Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
    - sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest
transformation sequence from beginWord to endWord, or 0 if no such sequence exists.

Example 1:
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.
Example 2:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: 0
Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.

Constraints:
1 <= beginWord.length <= 10
endWord.length == beginWord.length
1 <= wordList.length <= 5000
wordList[i].length == beginWord.length
beginWord, endWord, and wordList[i] consist of lowercase English letters.
beginWord != endWord
All the words in wordList are unique.
"""
import string
from collections import deque, defaultdict


def ladder_length(begin_word: str, end_word: str, words: list[str]):
    if end_word not in words or not end_word or not begin_word or not words:
        return 0

    length = len(begin_word)

    # Dictionary to hold combination of words that can be formed,
    # from any given word. By changing one letter at a time
    dictionary = defaultdict(list)
    for word in words:
        for i in range(length):
            dictionary[word[:i] + "*" + word[i+1:]].append(word)

    queue = deque([(begin_word, 1)])
    visited = set()
    visited.add(begin_word)

    while queue:
        # pop the leftmost word in queue
        # for each transformation of the current word, find from dictionary if there exists a word equal to end word.
        current_word, level = queue.popleft()
        for i in range(length):
            possible_word = current_word[:i] + "*" + current_word[i+1:]
            for word in dictionary[possible_word]:
                if word == end_word:
                    return level + 1

                if word not in visited:
                    visited.add(word)
                    queue.append((word, level + 1))
    return 0


def word_ladder_using_bidirectional_bfs(begin_word: str, end_word: str, words: list[str]):
    front = {begin_word}
    back = {end_word}
    depth = 1

    words = set(words)
    if end_word not in words:
        return 0

    def generate_possible_words(word):
        for i in range(len(word)):
            for c in string.ascii_lowercase:
                if c != word[i]:
                    yield word[:i] + c + word[i + 1:]

    seen = set()
    seen.add(begin_word)

    while front and back:
        if len(front) > len(back):  # pick the smaller group for next BFS iteration
            front, back = back, front
        next_front = set()
        for word in front:
            for possible_word in generate_possible_words(word):
                if possible_word in back:
                    return depth + 1
                if possible_word in words and possible_word not in seen:
                    seen.add(possible_word)
                    next_front.add(possible_word)
        front, depth = next_front, depth + 1
    return 0


# T O(n * m * m)
def word_ladder(begin_word: str, end_word:str, words: list[str]):
    if end_word not in words:
        return 0
    dictionary = defaultdict(list)
    for word in words:
        for i in range(len(word)):
            pattern = word[:i] + "*" + word[i+1:]
            dictionary[pattern].append(word)

    visit = set()
    visit.add(begin_word)

    queue = deque([begin_word])
    res = 1
    while queue:
        for i in range(len(queue)):
            current_word = queue.popleft()
            if current_word == end_word:
                return res

            for j in range(len(current_word)):
                pattern = current_word[:j] + "*" + current_word[j+1:]

                for possible_word in dictionary[pattern]:
                    if possible_word not in visit:
                        visit.add(possible_word)
                        queue.append(possible_word)

        res += 1
    return 0


def main():
    print(ladder_length("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
    # print(word_ladder_using_bidirectional_bfs("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
    print(word_ladder("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
    # print(ladder_length("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))


if __name__ == '__main__':
    main()

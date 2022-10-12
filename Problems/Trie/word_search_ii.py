"""
Given an m x n board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are
horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

Example 1:
Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]],
words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]
"""
from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.children = {}
        self.word_end = False

    def insert(self, word):
        curr = self
        for char in word:
            curr = curr.children.setdefault(char, TrieNode())
        curr.word_end = True


def word_search(board: list[list], words: list[str]) -> list[str]:
    root = TrieNode()
    for word in words:
        root.insert(word)

    rows, cols = len(board), len(board[0])
    num_words = len(words)
    result = []

    def dfs(row, col, node, path, num_words, result):
        if num_words == 0:
            return

        if node.word_end:
            result.append(path)
            node.word_end = False
            num_words -= 1

        if (row < 0 or col < 0 or
                row == rows or col == cols):
            return

        temp = board[row][col]

        if temp not in node.children:
            return

        board[row][col] = '#'

        for x, y in [[0, -1], [0, 1], [-1, 0], [1, 0]]:
            dfs(row + x, col + y, node.children[temp], path + temp, num_words, result)

        board[row][col] = temp

    for r in range(rows):
        for c in range(cols):
            dfs(r, c, root, "", num_words, result)

    return result


"""
Complexity.
- space complexity of trie is O(k), where k is sum of length of all words.
- Time complexity is O(mn*3^T), where m and n are sizes of our board and T is the length of the longest word in words. 
    Why? Because we start our dfs from all points of our board and do not stop until we make sure that the longest word 
    is checked: if we are not lucky and this word can not be found on board we need to check potentialy to the length T.
- Why 3^T? Because each time we can choose one of three directions, except the one we came from.
"""


class TNode:
    def __init__(self):
        self.children = defaultdict(TNode)
        self.is_word = False


class Trie2:
    def __init__(self):
        self.root = TNode()

    def insert(self, word):
        node = self.root
        for w in word:
            node = node.children[w]
        node.is_word = True

    def search(self, word):
        node = self.root
        for w in word:
            node = node.children.get(w)
            if not node:
                return False
        return node.is_word


def find_words(board, words):
    res = []
    trie = Trie2()
    node = trie.root
    for w in words:
        trie.insert(w)

    def dfs(board, node, i, j, path, res):
        if node.is_word:
            res.append(path)
            node.is_word = False
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return
        tmp = board[i][j]
        node = node.children.get(tmp)
        if not node:
            return
        board[i][j] = "#"
        dfs(board, node, i + 1, j, path + tmp, res)
        dfs(board, node, i - 1, j, path + tmp, res)
        dfs(board, node, i, j - 1, path + tmp, res)
        dfs(board, node, i, j + 1, path + tmp, res)
        board[i][j] = tmp

    for i in range(len(board)):
        for j in range(len(board[0])):
            dfs(board, node, i, j, "", res)
    return res

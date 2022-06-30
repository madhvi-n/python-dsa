"""
Given an m x n board of characters and a list of strings words, return all words on the board.
Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or
vertically neighboring. The same letter cell may not be used more than once in a word.

Example 1:
Input:  board = [["o","a","a","n"], ["e","t","a","e"], ["i","h","k","r"], ["i","f","l","v"]],
        words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]
"""


class TrieNode:
    def __init__(self):
        self.children = {}
        self.word_end = False

    def insert(self, word):
        curr = self
        for char in word:
            curr = curr.children.setdefault(char, TrieNode())
        curr.word_end = True


def word_search(board: list[list[str]], words: list[str]) -> bool:
    root = TrieNode()
    for word in words:
        root.insert(word)

    rows, cols = len(board), len(board[0])
    num_words = len(words)
    result = []

    def dfs(row, col, node, path, result):
        nonlocal num_words
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
            dfs(row + x, col + y, node.children[temp], path + temp, result)

        board[row][col] = temp

    for r in range(rows):
        for c in range(cols):
            dfs(r, c, root, "", result)

    return result


def word_search_ii(board: list[list], words: list[str]) -> bool:
    root = TrieNode()

    for word in words:
        root.insert(word)

    rows = len(board)
    cols = len(board)
    result, visited = set(), set()

    def dfs(row, col, node, word):
        if row < 0 or col < 0 or row >= rows or col >= cols or \
                (row, col) in visited or board[row][col] not in node.children:
            return

        visited.add((row, col))
        node = node.children[board[row][col]]
        word += board[row][col]

        if node.word_end:
            result.add(word)

        dfs(row + 1, col, node, word)
        dfs(row - 1, col, node, word)
        dfs(row, col + 1, node, word)
        dfs(row, col - 1, node, word)
        visited.remove((row, col))

    for r in range(rows):
        for c in range(cols):
            dfs(r, c, root, "")

    return list(result)


def main():
    board = [["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]]
    print(word_search(board, ["oath", "pea", "eat", "rain"]))
    print(word_search_ii(board, ["oath", "pea", "eat", "rain"]))


if __name__ == '__main__':
    main()

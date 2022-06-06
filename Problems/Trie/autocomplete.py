class TrieNode:
    def __init__(self):
        self.children = {}
        self.word_end = False


def insert(head, word):
    curr = head
    for char in word:
        curr = curr.children.setdefault(char, TrieNode())
    curr.word_end = True


def suggestions(node, word, res):
    if node.word_end:
        res.append(word)

    for (k, node) in node.children.items():
        suggestions(node,  word + k, res)
    return res


def autocomplete(root: TrieNode, search_word: str, res=[]) -> None:
    curr = root

    for char in search_word:
        if char not in curr.children:
            return
        curr = curr.children[char]

    if not curr.children:
        return

    return suggestions(curr, search_word, res)


def main():
    words = [
        'code', 'coding', 'recordable', 'codependency', 'codex', 'codify',
        'codependents', 'codes', 'code', 'coder', 'codesign', 'codec',
        'ball', 'blue', 'bag', 'bagged', 'moon', 'dream'
    ]

    head = TrieNode()
    for word in words:
        insert(head, word)

    print("Suggestions for cod:", autocomplete(head, "cod"))


if __name__ == '__main__':
    main()

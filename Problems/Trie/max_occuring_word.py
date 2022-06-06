class TrieNode:
    def __init__(self):
        self.key = None
        self.count = 0
        self.children = {}


def insert(head, word):
    curr = head

    for char in word:
        curr = curr.children.setdefault(char, TrieNode())
    curr.key = word
    curr.count += 1


def max_occuring_word(root):
    def preorder(curr, key="", max_count=0):
        if curr is None:
            return key, max_count

        for (k, node) in curr.children.items():
            if max_count < node.count:
                key = node.key
                max_count = node.count

            # recur for current node's children
            key, max_count = preorder(node, key, max_count)
        return key, max_count
    return preorder(root)


def main():
    words = [
        'code', 'coder', 'coding', 'codable', 'codec', 'codecs', 'coded',
        'codeless', 'codec', 'codecs', 'codependence', 'codex', 'codify',
        'codependents', 'codes', 'code', 'coder', 'codesign', 'codec',
        'codeveloper', 'codrive', 'codec', 'codecs', 'codiscovered'
    ]

    head = TrieNode()
    for word in words:
        insert(head, word)

    key, count = max_occuring_word(head)
    print(f"Word: {key}, Count: {count}")


if __name__ == '__main__':
    main()

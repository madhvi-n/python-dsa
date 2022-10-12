"""
Design a map that allows you to do the following:
Maps a string key to a given value.
Returns the sum of the values that have a key with a prefix equal to a given string.
Implement the MapSum class:

MapSum() Initializes the MapSum object.
void insert(String key, int val) Inserts the key-val pair into the map.
If the key already existed, the original key-value pair will be overridden to the new one.
int sum(string prefix) Returns the sum of all the pairs' value whose key starts with the prefix.

Example 1:
Input
["MapSum", "insert", "sum", "insert", "sum"]
[[], ["apple", 3], ["ap"], ["app", 2], ["ap"]]
Output
[null, null, 3, null, 5]

Explanation:
mapSum = new MapSum();
mapSum.insert("apple", 3);
mapSum.sum("ap");           // return 3 (apple = 3)
mapSum.insert("app", 2);
mapSum.sum("ap");           // return 5 (apple + app = 3 + 2 = 5)
"""


class TrieNode:
    def __init__(self):
        self.children = {}
        self.frequency = 0


class MapSum:

    def __init__(self):
        self.root = TrieNode()
        self.dict = {}

    def insert(self, key: str, val: int) -> None:
        delta = val - self.dict.get(key, 0)
        self.dict[key] = val
        curr = self.root
        curr.frequency += delta
        for char in key:
            curr = curr.children.setdefault(char, TrieNode())
            curr.frequency += delta

    def sum(self, prefix: str) -> int:
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return 0
            curr = curr.children[char]
        return curr.frequency

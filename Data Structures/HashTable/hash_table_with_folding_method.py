"""
https://www.geeksforgeeks.org/folding-method-in-hashing/?ref=rp

Algorithm:
The folding method is used for creating hash functions starts with the item being divided into equal-sized pieces
i.e., the last piece may not be of equal size.

The outcome of adding these bits together is the hash value, H(x) = (a + b + c) mod M, where a, b, and c represent
the preconditioned key broken down into three parts and M is the table size, and mod stands for modulo.

In other words, the sum of three parts of the preconditioned key is divided by the table size. The remainder is the hash key.
"""


class HashTable:
    def __init__(self, MAX_SIZE=100):
        self.MAX_SIZE = MAX_SIZE
        self.arr = [None for _ in range(self.MAX_SIZE)]

    def get_hash(self, key):
        # split key into three segments
        a, b, c = 1, 1, 1
        h = a + b + c
        return h % self.MAX_SIZE

    def __setitem__(self, key, val):
        arr_index = self.get_hash(key)
        self.arr[arr_index] = val

    def __getitem__(self, key):
        arr_index = self.get_hash(key)
        return self.arr[arr_index]

    def __delitem__(self, key):
        arr_index = self.get_hash(key)
        self.arr[arr_index] = None

    def __repr__(self):
        return self.arr

    def __str__(self):
        return f"{self.arr}"


def main():
    pass


if __name__ == '__main__':
    main()

"""
Another numerical technique for constructing a hash function is called the mid-square method.
We first square the item, and then extract some portion of the resulting digits.

For example, if the item were 44, we would first compute 44**2=1,936. By extracting the middle two digits, 93,
and performing the remainder step, we get 5 (93 % 11)
"""


class HashTable:
    def __init__(self, MAX_SIZE=100):
        self.MAX_SIZE = MAX_SIZE
        self.arr = [None for _ in range(self.MAX_SIZE)]

    def get_hash(self, key):
        # Square the key and find the middle two digits
        key = key ** 2
        print(key)
        mid = (len(str(key)) // 2)
        print(mid)
        h = str(key)[mid-1:mid+1]
        return int(h) % self.MAX_SIZE

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
    t = HashTable()
    print(t.get_hash(44))
    print()
    print(t.get_hash(46))

    print()
    print(t.get_hash(123456789))


if __name__ == '__main__':
    main()

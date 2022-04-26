class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [None for _ in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX

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
    t["march 6"] = 310
    t["march 7"] = 420
    t["march 8"] = 67
    t["march 17"] = 634
    print(t)


if __name__ == '__main__':
    main()

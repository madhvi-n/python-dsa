class TreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def number_of_trees(n):
    arr = [1, 1]

    for i in range(2, n + 1):
        arr.append(0)
        for j in range(0, i):
            arr[i] += arr[j] * arr[i-j-1]
    return arr[-1]


def main():
    print(number_of_trees(4))
    print(number_of_trees(5))
    print(number_of_trees(10))


if __name__ == '__main__':
    main()

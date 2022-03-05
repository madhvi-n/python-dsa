"""
You are given a string s and an integer array indices of the same length. The string s will be shuffled such that the character at the ith position moves to indices[i] in the shuffled string.

Return the shuffled string.

Input: s = "codeleet", indices = [4,5,6,7,0,2,1,3]
Output: "leetcode"
Explanation: As shown, "codeleet" becomes "leetcode" after shuffling.
"""

from typing import List

def shuffle_array(s: str, indices: List[int]) -> str:
    res = [0] * len(indices)

    for i, j in zip(s, indices):
        res[j] = i
        print(res)

    return "".join(res)


def main():
    result = shuffle_array("codeleet", [4,5,6,7,0,2,1,3])
    print(result)

if __name__ == '__main__':
    main()

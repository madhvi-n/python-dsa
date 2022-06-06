"""
Given a list of words, efficiently group all anagrams. The two strings, X and Y, are anagrams if by rearranging X's
letters, we can get Y using all the original letters of X exactly once.

Input : [
    'CARS', 'REPAID', 'DUES', 'NOSE', 'SIGNED', 'LANE',
    'PAIRED', 'ARCS', 'GRAB', 'USED', 'ONES',
    'BRAG', 'SUED', 'LEAN', 'SCAR', 'DESIGN'
]

Output:
{
    ('CARS', 'ARCS', 'SCAR'),
    ('REPAID', 'PAIRED'),
    ('SIGNED', 'DESIGN'),
    ('LANE', 'LEAN'),
    ('GRAB', 'BRAG'),
    ('NOSE', 'ONES'),
    ('DUES', 'USED', 'SUED')
}


Input : ['CARS', 'LANE', 'ONES']
Output: {}

The solution should return a set containing all the anagrams grouped together, irrespective of the order.
"""
from collections import defaultdict


def group_anagrams(words: list[str]) -> list[list]:
    return []


# Time O(nlogn) and Space O(n)
def group_anagrams_ii(words: list[str]) -> list[list]:
    counter = defaultdict(list)
    for word in words:
        w = "".join(sorted(word))
        counter[w] += [word]

    result = []
    for values in counter.values():
        if len(values) > 1:
            result.append(values)
    return result


def main():
    words = [
        'CARS', 'REPAID', 'DUES', 'NOSE', 'SIGNED', 'LANE',
        'PAIRED', 'ARCS', 'GRAB', 'USED', 'ONES',
        'BRAG', 'SUED', 'LEAN', 'SCAR', 'DESIGN'
    ]

    print(group_anagrams_ii(words))
    print(group_anagrams_ii(['CARS', 'REPAID', 'DUES']))


if __name__ == '__main__':
    main()

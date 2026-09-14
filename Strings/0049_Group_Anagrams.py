"""
Problem:
49. Group Anagrams

Difficulty:
Medium

Topics:
String, Hash Table, Sorting

Approach:
Sort each string alphabetically and use the sorted string
as a key in a hash map. Strings with the same sorted key
belong to the same anagram group.

Time Complexity:
O(n * k log k)

Space Complexity:
O(n * k)

Where:
n = number of strings
k = maximum length of a string
"""

from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        result_list = []

        for s in strs:
            key = ''.join(sorted(s))
            dic.setdefault(key, []).append(s)

        for value in dic.values():
            result_list.append(value)

        return result_list
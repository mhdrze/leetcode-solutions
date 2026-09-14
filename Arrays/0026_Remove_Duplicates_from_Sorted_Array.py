"""
Problem:
26. Remove Duplicates from Sorted Array

Difficulty:
Easy

Topics:
Array, Hash Table

Approach:
Use a dictionary to keep track of unique numbers.
After collecting unique values, rewrite the beginning
of the array with those values and return the number
of unique elements.

Time Complexity:
O(n)

Space Complexity:
O(n)

Where:
n = length of nums
"""

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        dic = {}
        i = 0

        for num in nums:
            if num not in dic:
                dic[num] = i
                i += 1

        for key, value in dic.items():
            nums[value] = key

        return i
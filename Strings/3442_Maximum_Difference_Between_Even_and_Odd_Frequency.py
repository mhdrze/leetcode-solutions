"""
Problem:
3442. Maximum Difference Between Even and Odd Frequency

Difficulty:
Easy

Topics:
String, Hash Table

Approach:
Count the frequency of each character using a dictionary.
Separate frequencies into even and odd groups, then return
the difference between the maximum odd frequency and the
minimum even frequency.

Time Complexity:
O(n)

Space Complexity:
O(k)

Where:
n = length of the string
k = number of unique characters
"""


class Solution:
    def maxDifference(self, s: str) -> int:
        frequency = {}

        for char in s:
            if char in frequency:
                frequency[char] += 1
            else:
                frequency[char] = 1

        values = list(frequency.values())

        even = [x for x in values if x % 2 == 0]
        odd = [x for x in values if x % 2 != 0]

        return max(odd) - min(even)
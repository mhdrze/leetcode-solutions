"""
Problem:
3110. Score of a String

Difficulty:
Easy

Topics:
String

Approach:
Calculate the sum of absolute differences between the ASCII
values of every pair of adjacent characters.

Time Complexity:
O(n)

Space Complexity:
O(1)

Where:
n = length of the string
"""


class Solution:
    def scoreOfString(self, s: str) -> int:
        total = 0

        for char in range(0, len(s) - 1):
            total += abs(ord(s[char]) - ord(s[char + 1]))

        return total
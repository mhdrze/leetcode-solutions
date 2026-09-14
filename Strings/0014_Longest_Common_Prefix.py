"""
Problem:
14. Longest Common Prefix

Difficulty:
Easy

Topics:
String

Approach:
Find the shortest string because the common prefix cannot
be longer than it. Then compare each character position
with all strings until a mismatch is found.

Time Complexity:
O(n * m)

Space Complexity:
O(1)

Where:
n = number of strings
m = length of the shortest string
"""

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        smll = min(strs, key=len)

        for i in range(len(smll)):
            for item in strs:
                if smll[i] != item[i]:
                    return smll[:i]

        return smll
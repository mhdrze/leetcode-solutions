"""
Problem:
13. Roman to Integer

Difficulty:
Easy

Topics:
Hash Table, Math, String

Approach:
Store Roman numeral values in a dictionary.
While iterating through the string, if the current value
is smaller than the next value, subtract it. Otherwise,
add it to the result.

Time Complexity:
O(n)

Space Complexity:
O(1)
"""

class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0
        i = 0

        while i < len(s):
            if i < len(s) - 1 and dic[s[i]] < dic[s[i + 1]]:
                total += dic[s[i + 1]] - dic[s[i]]
                i += 2
            else:
                total += dic[s[i]]
                i += 1

        return total
"""
Problem:
242. Valid Anagram

Difficulty:
Easy

Topics:
String, Hash Table

Approach:
Count the frequency of each character in the first string.
Then decrease the count while iterating through the second string.
If all frequencies become zero, the two strings are anagrams.

Time Complexity:
O(n)

Space Complexity:
O(n)
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic = {}

        for char in s:
            if char not in dic:
                dic[char] = 1
            else:
                dic[char] += 1

        for ch in t:
            if ch in dic:
                dic[ch] -= 1
            else:
                return False

        return all(value == 0 for value in dic.values())
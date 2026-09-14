"""
Problem:
3. Longest Substring Without Repeating Characters

Difficulty:
Medium

Topics:
String, Hash Table, Sliding Window

Approach:
Maintain a sliding window with two pointers.
The dictionary stores the latest index of each character.
When a repeated character appears inside the current window,
move the left pointer to the position after the previous occurrence.

Time Complexity:
O(n)

Space Complexity:
O(min(n, k))

Where:
k = size of the character set
"""




class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left_far_side = 0
        max_len = 0
        dic = {}

        for i in range(len(s)):
            if s[i] in dic and dic[s[i]] >= left_far_side:
                left_far_side = dic[s[i]] + 1

            dic[s[i]] = i
            max_len = max(max_len, i - left_far_side + 1)

        return max_len
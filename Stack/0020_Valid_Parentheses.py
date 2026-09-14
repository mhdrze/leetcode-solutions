"""
Problem:
20. Valid Parentheses

Difficulty:
Easy

Topics:
String, Stack

Approach:
Use a stack to store opening brackets.
When a closing bracket appears, compare it with the
most recent opening bracket stored in the stack.
The string is valid only if all brackets are matched.

Time Complexity:
O(n)

Space Complexity:
O(n)
"""


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parts = {")": "(", "]": "[", "}": "{"}

        for ch in s:
            if ch in parts.values():
                stack.append(ch)

            elif ch in parts:
                if not stack or stack[-1] != parts[ch]:
                    return False

                stack.pop()

        return not stack
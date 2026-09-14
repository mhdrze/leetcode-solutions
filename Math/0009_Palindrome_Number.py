"""
Problem:
9. Palindrome Number

Difficulty:
Easy

Topics:
Math, String

Approach:
Convert the number into a string and compare it with its
reversed version. If both strings are identical, the number
is a palindrome.

Time Complexity:
O(n)

Space Complexity:
O(n)

Where:
n = number of digits
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        y = x[::-1]

        if x == y:
            return True
        else:
            return False

"""
    Problem Statement: https://leetcode.com/problems/length-of-last-word/
    Author: Meer Husamuddin

    Time Complexity: O(N)
    Space Complexity: O(1)
"""
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1
        while i >= 0 and s[i] == " ":
            i -= 1
        length = 0
        while i >= 0 and s[i] != " ":
            length += 1
            i -= 1
        return length
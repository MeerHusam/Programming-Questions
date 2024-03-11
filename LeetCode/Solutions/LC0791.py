"""
    Problem Statement: https://leetcode.com/problems/custom-sort-string/
    Author: Meer Husamuddin

    Time Complexity: O(N + M)
    Space Complexity: O(N)
"""

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        string = ""
        occurences = [0] * 26
        # Add th occurences
        for a in s:
            occurences[ord(a) - ord('a')] += 1
        # Add the letter which are in order
        for a in order:
            while occurences[ord(a) - ord('a')] > 0:
                string += a
                occurences[ord(a) - ord('a')] -= 1
        for a in range(26):
            while occurences[a] > 0:
                string += chr(a + ord('a'))
                occurences[a] -= 1
        return string
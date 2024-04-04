"""
    Problem Statement: https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/
    Author: Meer Husamuddin

    Time Complexity: O(N)
    Space Complexity: O(1)
"""
class Solution:
    def maxDepth(self, s: str) -> int:
        count = 0
        max_count = 0
        for char in s:
            if char == "(":
                count += 1
            elif char == ")":
                count -= 1
            max_count = max(max_count, count)
        return max_count
"""
    Problem Statement: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/
    Author: Meer Husamuddin

    Time Complexity: O(N*M)
    Space Complexity: O(1)
"""
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return -1
        lengthNeedle, lengthHaystack = len(needle), len(haystack)
        curr_length = a = 0
        while(a < lengthHaystack):
            if haystack[a] == needle[curr_length]:
                curr_length += 1
                if curr_length == lengthNeedle:
                    return a - curr_length + 1
                a += 1               
            else:
                a = a - curr_length
                a += 1
                curr_length = 0
        return -1
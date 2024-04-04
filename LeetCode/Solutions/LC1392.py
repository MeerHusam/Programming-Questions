"""
    Problem Statement: https://leetcode.com/problems/longest-happy-prefix/
    Author: Meer Husamuddin

    Time Complexity: O(N)
    Space Complexity: O(N)
"""
class Solution:
    def longestPrefix(self, s: str) -> str:
        # Just compute KMP Algo LPSArray
        lps = [0] * len(s)
        prev_lps = 0
        i = 1
        length = len(s)
        while i < length:
            if s[i] == s[prev_lps]:
                lps[i] = prev_lps + 1
                prev_lps += 1
                i += 1
            elif prev_lps == 0:
                lps[i] = 0
                i += 1
            else:
                prev_lps = lps[prev_lps - 1]
        return s[:lps[-1]]
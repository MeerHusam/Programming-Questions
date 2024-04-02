"""
    Problem Statement: https://leetcode.com/problems/isomorphic-strings
    Author: Meer Husamuddin

    Time Complexity: O(N)
    Space Complexity: O(N)
"""
from collections import defaultdict
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count_s = defaultdict(list)
        count_t = defaultdict(list)
        for i in range(len(s)):
            count_s[s[i]].append(i)
            count_t[t[i]].append(i)
        if list(count_s.values()) != list(count_t.values()):
            return False
        return True
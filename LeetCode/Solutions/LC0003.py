"""
Problem Statement: https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
Author: Meer Husamuddin, https://github.com/MeerHusam/
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        i = j = size = 0
        while i < len(s):
            while s[i] in char_set:
                char_set.remove(s[j])
                j += 1
            
            char_set.add(s[i])
            size = max(size, i - j + 1)
            i += 1
        
        return size
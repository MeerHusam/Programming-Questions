"""
    Problem Statement: https://leetcode.com/problems/shortest-palindrome/
    Author: Meer Husamuddin

    Time Complexity: O(N^2) (for the starts with method)
    Space Complexity: O(N) (to create the reverse string)
"""
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        def find_pattern(s, reverse):
            for i in range(len(s)):
                if s.startswith(reverse[i:]):
                    return i
            return 0
         
        reverse = s[::-1]
        if s == reverse:
            return reverse
        # Find the length of the longest common pattern
        #    abcd
        # dcba
        # The length here would be 1
        length = find_pattern(s, reverse)
        return reverse[:length] + s
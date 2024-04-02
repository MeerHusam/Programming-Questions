"""
    Problem Statement: https://leetcode.com/problems/longest-palindromic-substring/
    Author: Meer Husamuddin

    Time Complexity: O(N^2)
    Space Complexity: O(1)
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def helper(index, left, right):
            output = [0, 0]
            while left >= 0 and right < len(s) and s[left] == s[right]:
                output = [left, right]
                left -= 1
                right += 1

            return output

        longest_index = [0, 0]
        for index in range(len(s)):
            # Check for odd
            string_odd = helper(index, index - 1, index + 1)
            # Check for even
            string_even = helper(index, index, index + 1)
            if string_odd[1] - string_odd[0] > string_even[1] - string_even[0]:
                curr_longest = string_odd
            else:
                curr_longest = string_even
            if longest_index[1] - longest_index[0] < curr_longest[1] - curr_longest[0]:
                longest_index = curr_longest

        return s[longest_index[0]: longest_index[1] + 1]
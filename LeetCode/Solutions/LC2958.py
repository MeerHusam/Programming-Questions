"""
    Problem Statement: https://leetcode.com/problems/length-of-longest-subarray-with-at-most-k-frequency
    Author: Meer Husamuddin

    Time Complexity: O(N)
    Space Complexity: O(N)
"""
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        freq = {}
        i = j = length = 0
        for j in range(len(nums)):
            if nums[j] in freq:
                freq[nums[j]] += 1
            else:
                freq[nums[j]] = 1
            while freq[nums[j]] > k:
                freq[nums[i]] -= 1
                i += 1
            length = max(length, j + 1 - i)
        return length
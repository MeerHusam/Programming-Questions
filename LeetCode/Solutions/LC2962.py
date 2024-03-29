"""
    Problem Statement: https://leetcode.com/problems/count-subarrays-where-max-element-appears-at-least-k-times
    Author: Meer Husamuddin

    Time Complexity: O(N)
    Space Complexity: O(1)
"""
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_val = max(nums)
        result = i = max_elems_in_window = 0
        for j in range(len(nums)):
            if nums[j] == max_val:
                max_elems_in_window += 1
            while max_elems_in_window == k:
                if nums[i] == max_val:
                    max_elems_in_window -= 1
                i += 1
            result += i
        return result
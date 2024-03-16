"""
    Problem Statement: https://leetcode.com/problems/contiguous-array/description/
    Author: Meer Husamuddin

    Time Complexity: O(N)
    Space Complexity: O(N)
"""
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        indices = {}
        curr_max = prefix_sum = 0
        for index in range(len(nums)):
            prefix_sum += 1 if nums[index] == 1 else -1
            if prefix_sum == 0:
                curr_max = index + 1
            elif prefix_sum in indices:
                indices[prefix_sum][1] = index
                sum = index - indices[prefix_sum][0]
                curr_max = sum if sum > curr_max else curr_max
            else:
                indices[prefix_sum] = [index, None]
        return curr_max
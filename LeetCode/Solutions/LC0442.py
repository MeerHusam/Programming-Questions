"""
    Problem Statement: https://leetcode.com/problems/find-all-duplicates-in-an-array/
    Author: Meer Husamuddin

    Time Complexity: O(N)
    Space Complexity: O(1)
"""
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        output = []
        for index, a in enumerate(nums):
            if nums[abs(a) - 1] < 0:
                output.append(abs(a))
            else:
                nums[abs(a) - 1] = -nums[abs(a) - 1]
        return output
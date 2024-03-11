"""
    Problem Statement: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
    Author: Meer Husamuddin
    Time Complexity: O(N)
    Space Complexity: O(1)
"""
class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        j = 1
        length = len(nums)
        for i in range(1, length):
            if nums[i] != nums[i-1]:
                nums[j] = nums[i]
                j += 1
        return j
"""
    Problem Statement: https://leetcode.com/problems/remove-element/description/
    Author: Meer Husamuddin
    Time Complexity: O(N)
    Space Complexity: O(1)
"""
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for value in nums:
            if value != val:
                nums[k] = value
                k += 1
        return k
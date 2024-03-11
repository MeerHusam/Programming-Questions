"""
    Problem Statement: https://leetcode.com/problems/intersection-of-two-arrays/
    Author: Meer Husamuddin, https://github.com/MeerHusam/
    Time Complexity: O(M + N)
    Space Complexity: O(M + N)
"""
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersection = set()
        set1 = set(nums1)
        set2 = set(nums2)
        for val in set1:
            if val in set2:
                intersection.add(val)   
        return intersection
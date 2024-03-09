"""
Problem Statement: https://leetcode.com/problems/minimum-common-value/description/
Author: Meer Husamuddin, https://github.com/MeerHusam/
"""
class Solution:
    def getCommon(self, nums1, nums2) -> int:
        i = j = 0
        length1, length2 =  len(nums1), len(nums2)
        while True:
            if nums1[i] < nums2[j]:
                i = i + 1 if i < length1 - 1 else i
            if nums2[j] < nums1[i]:
                j = j + 1 if j < length2- 1 else j
            if nums1[i] == nums2[j]:
                return nums1[i]    
            if i == len(nums1) -1 or j == len(nums2) - 1:
                return -1              
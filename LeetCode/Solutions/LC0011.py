"""
Problem Statement: https://leetcode.com/problems/container-with-most-water/description/
Author: Meer Husamuddin, https://github.com/MeerHusam/
"""
class Solution:
    def maxArea(self, height: List[int]) -> int:
        pointer_1 = 0
        pointer_2 = len(height) -1
        max_area = 0
        for i in range(len(height)):
            if height[pointer_1] < height[pointer_2]:
                # calc area 
                area =  height[pointer_1] * (pointer_2-pointer_1)
                pointer_1 += 1 
            else:
                area =  height[pointer_2] * (pointer_2-pointer_1)
                pointer_2 -= 1

            if area > max_area:
                max_area = area

        return max_area  


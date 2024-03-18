"""
    Problem Statement: https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/
    Author: Meer Husamuddin

    Time Complexity: O(N log N)
    Space Complexity: O(1)
"""
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if len(points) == 1:
            return 1
        points.sort()
        count = 1
        for a in range(1, len(points)):
            if points[a][0] > points[a - 1][1]:
                count += 1
            else:
                # Balloon is burst
                points[a][1] = min(points[a - 1][1], points[a][1])
        return count
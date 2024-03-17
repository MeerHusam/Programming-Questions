"""
    Problem Statement: https://leetcode.com/problems/insert-interval/description/
    Author: Meer Husamuddin

    Time Complexity: O(N logN)
    Space Complexity: O(N)
"""
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        overlaps = []
        returnList = []
        for index, val in enumerate(intervals):
            start = newInterval[0]
            end = newInterval[1]
            # The new interval starts within an existing interval
            if start >= val[0] and start <= val[1]:
                overlaps.append(val)
            # The new interval completely covers an existing interval
            elif (start <= val[0] and start <= val[1]) and end >= val[1]:
                overlaps.append(val)
            # The new interval ends within an existing interval
            elif end <= val[1] and end >= val[0]:
                overlaps.append(val)
            else:
            # No overlap
                returnList.append(val)
        outputIntervals = []
        if overlaps:
            # Add the newly created interval in the return intervals array
            returnList.append([min(newInterval[0], overlaps[0][0]), max(newInterval[1], overlaps[len(overlaps) - 1][1])])
        else:
            # Add the new interval(given) in the return array
            returnList.append(newInterval) 
        returnList.sort()
        return returnList
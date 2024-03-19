"""
    Problem Statement: https://leetcode.com/problems/task-scheduler/description/
    Author: Meer Husamuddin

    Time Complexity: O(N * M) where M is the cooldown
    Space Complexity: O(N)
"""
from collections import Counter, deque
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Creates a HashMap with the freq
        counts = Counter(tasks)
        maxHeap = [-count for count in counts.values()]
        heapq.heapify(maxHeap)

        time = 0 
        q = deque()
        while q or maxHeap:
            time += 1
            if maxHeap:
                value = heapq.heappop(maxHeap) + 1
                if value != 0:
                    q.append([value, time + n])
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        return time
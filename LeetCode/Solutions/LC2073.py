"""
    Problem Statement: https://leetcode.com/problems/time-needed-to-buy-tickets/
    Author: Meer Husamuddin

    Time Complexity: O(N)
    Space Complexity: O(1)
"""
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        num_tickets = tickets[k]
        time = 0
        for index,a in enumerate(tickets):
            if a >= num_tickets:
                if index > k:
                    time -= 1
                time += num_tickets
            else:
                time += a
        return time
        
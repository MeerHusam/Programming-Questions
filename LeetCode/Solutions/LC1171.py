"""
    Problem Statement: https://leetcode.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list/
    Author: Meer Husamuddin

    Time Complexity: O(N)
    Space Complexity: O(N)
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeZeroSumSublists(self, head):
        newHead = ListNode(0)
        newHead.next = head
        iter = head

        prefix_sum = 0
        prefix_sum_map = {}
        while iter != None:
            prefix_sum += iter.val
            prefix_sum_map[prefix_sum] = iter
            iter = iter.next

        iter = newHead
        prefix_sum = 0
        while iter != None:
            prefix_sum += iter.val
            # Consider the LinkedList = [1, 2, -3, 3, 1] and its prefix sums = [1, 3, 0, 3, 4].
            # Observing the prefix sums, when a sum repeats (like '3' in this example), it indicates
            # that the sub-list between these two points sums to zero and should be removed.
            # This operation leaves us with [1, 2, 1], removing the elements between the two occurrences of '3'.
            if prefix_sum in prefix_sum_map:
                # Link the current node to the node after the last occurrence of this sum
                curr.next = prefix_sum_map[prefix_sum].next
            curr = curr.next

        return newHead.next
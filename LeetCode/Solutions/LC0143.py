"""
    Problem Statement: https://leetcode.com/problems/reorder-list/
    Author: Meer Husamuddin

    Time Complexity: O(N)
    Space Complexity: O(1)
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
        
        slow = fast = head
        prev = None
        # prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        # Reverse
        prev.next = None
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp

        iter = head
        temp = iter.next
        iter.next = prev
        iter = temp
        while iter:
            temp = iter.next
            iter.next = prev.next
            prev.next = iter
            prev = iter.next
            iter = temp
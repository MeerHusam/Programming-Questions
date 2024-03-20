"""
    Problem Statement: https://leetcode.com/problems/linked-list-cycle-ii/description/
    Author: Meer Husamuddin

    Time Complexity: O(N)
    Space Complexity: O(1)
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        slow = fast = head
        while fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                break
        if fast.next == None or fast.next.next == None:
            return None
        fast = head
        while fast != slow:
            fast = fast.next
            slow = slow.next
        return slow
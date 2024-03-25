"""
    Problem Statement: https://leetcode.com/problems/palindrome-linked-list
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
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True

        slow = head.next
        fast = head.next.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        reversed_list = self.reverseList(slow)

        while reversed_list and head:
            if reversed_list.val != head.val:
                return False
            head = head.next
            reversed_list = reversed_list.next

        return True

    def reverseList(self, head):
        prev = None
        current = head

        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        return prev
/*
 * Problem Statement:https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
 * Author: Meer Husamuddin, https://github.com/MeerHusam/
 */
package LeetCode.Solutions;

//  * Definition for singly-linked list.
class ListNode {
    int val;
    ListNode next;

    ListNode() {
    }

    ListNode(int val) {
        this.val = val;
    }

    ListNode(int val, ListNode next) {
        this.val = val;
        this.next = next;
    }
}

class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        if (head.next == null)
            return head.next;

        int size = 0;
        ListNode iter = head;

        while (iter != null) {
            ++size;
            iter = iter.next;
        }

        if (size - n == 0)
            return head.next;

        iter = head;
        for (int i = 0; i < size - n - 1; i++)
            iter = iter.next;
        iter.next = iter.next.next;
        return head;
    }
}
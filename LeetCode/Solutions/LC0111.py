"""
    Problem Statement: https://leetcode.com/problems/minimum-depth-of-binary-tree/
    Author: Meer Husamuddin

    Time Complexity: O(N)
    Space Complexity: O(1)
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = [[root, 1]]
        while queue:
            value, depth = queue.pop(0)
            if not value.right and not value.left:
                return depth
            if value.left:
                queue.append([value.left, depth + 1])
            if value.right:
                queue.append([value.right, depth + 1])
        return 
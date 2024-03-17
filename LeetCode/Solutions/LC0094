"""
    Problem Statement: https://leetcode.com/problems/binary-tree-inorder-traversal/
    Author: Meer Husamuddin

    Time Complexity: O(N)
    Space Complexity: O(N)
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        self = root
        def dfs(self):
            if self.left != None:
                dfs(self.left)
            output.append(self.val)
            if self.right != None:
                dfs(self.right)
            return
        if(self != None):
            dfs(self)
        return(output)
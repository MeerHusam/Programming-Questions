"""
    Problem Statement: https://leetcode.com/problems/longest-palindromic-substring/
    Author: Meer Husamuddin

    Time Complexity: O(N * M * 4^N)
    Space Complexity: O(N)
"""
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(a, b, index):
            if index == len(word):
                return True
            
            if a < 0 or a >= len(board) or b < 0 or b >= len(board[0]) or (a, b) in visited or word[index] != board[a][b]:
                return False
                        
            visited.add((a, b))
            # Explore all valid neighbors
            res = (dfs(a+1, b, index+1) or
                dfs(a-1, b, index+1) or
                dfs(a, b+1, index+1) or
                dfs(a, b-1, index+1))
            visited.remove((a, b))
            return res           
        
        visited = set()
        for a in range(len(board)):
            for b in range(len(board[0])):
                if word[0] == board[a][b]:
                    if dfs(a, b, 0):
                        return True
        return False
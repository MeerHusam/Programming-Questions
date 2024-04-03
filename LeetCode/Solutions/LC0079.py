"""
    Problem Statement: https://leetcode.com/problems/word-search/
    Author: Meer Husamuddin

    Time Complexity: O(N * M * 3^W)
    Space Complexity: O(N)
"""
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        if word.count(word[0]) > word.count(word[-1]):
            word = word[::-1]

        def dfs(a, b, index):
            if index == len(word):
                return True
            
            if a < 0 or a >= len(board) or b < 0 or b >= len(board[0]) or board[a][b] == "#" or word[index] != board[a][b]:
                return False
                        
            temp = board[a][b]
            board[a][b] = "#"
            # Explore all valid neighbors
            res = (dfs(a+1, b, index+1) or
                dfs(a-1, b, index+1) or
                dfs(a, b+1, index+1) or
                dfs(a, b-1, index+1))
            board[a][b] = temp
            return res           
        
        for a in range(len(board)):
            for b in range(len(board[0])):
                if word[0] == board[a][b]:
                    if dfs(a, b, 0):
                        return True
        return False
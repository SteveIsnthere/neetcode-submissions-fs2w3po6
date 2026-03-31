from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        
        def find_path(r: int, c: int, index: int, visited: set) -> bool:
            # Base case: if we've matched all characters in the word
            if index == len(word):
                return True
            
            # Out of bounds, wrong character, or already visited in this path
            if (r < 0 or r >= rows or 
                c < 0 or c >= cols or 
                board[r][c] != word[index] or 
                (r, c) in visited):
                return False
            
            # Mark current cell as visited
            visited.add((r, c))
            
            # Check all 4 directions for the next character
            # Using the distance logic (r2-r1)^2 + (c2-c1)^2 == 1
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for dr, dc in directions:
                if find_path(r + dr, c + dc, index + 1, visited):
                    return True
            
            # Backtrack: remove cell so it can be used in other path attempts
            visited.remove((r, c))
            return False

        # Your original idea: find all starting coordinates for the first letter
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    # Start the recursive path search from here
                    if find_path(r, c, 0, set()):
                        return True
                        
        return False

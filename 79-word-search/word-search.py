# class Solution(object):
#     def exist(self, board, word):
#         """
#         :type board: List[List[str]]
#         :type word: str
#         :rtype: bool
#         """
class Solution(object):
    def exist(self, board, word):
        if not board or not board[0]:
            return False  # Edge case: Empty board
        
        rows, cols = len(board), len(board[0])

        def dfs(r, c, index):
            # Base case: If index reaches length of word, we found the word
            if index == len(word):
                return True

            # Out of bounds or character mismatch or already visited
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[index]:
                return False

            # Temporarily mark cell as visited
            temp = board[r][c]
            board[r][c] = '#'

            # Explore all 4 possible directions (Up, Down, Left, Right)
            found = (dfs(r + 1, c, index + 1) or
                     dfs(r - 1, c, index + 1) or
                     dfs(r, c + 1, index + 1) or
                     dfs(r, c - 1, index + 1))

            # Restore cell for backtracking
            board[r][c] = temp
            
            return found

        # Start DFS from every cell
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0] and dfs(i, j, 0):
                    return True

        return False
        
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        count=0
        n=len(grid)

        cols=[[grid[row][col] for row in range(n)] for col in range(n)]

        for row in grid:
            for col in cols:
                if row==col:
                    count+=1
        return count

        
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        count=0
        n=len(grid)

# In Python, grids are usually lists of rows, but sometimes you want the columns too!

# This line creates a list called cols, where each item is a column from the grid.



        cols=[[grid[row][col] for row in range(n)] for col in range(n)]

        for row in grid:
            for col in cols:
                if row==col:
                    count+=1
        return count

        
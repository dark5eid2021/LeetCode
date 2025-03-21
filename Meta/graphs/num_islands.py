"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), 
return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
You may assume all four edges of the grid are all surrounded by water.

"""
from typing import List

class Solution:
    def dfs(self, grid, i, j):
        m, n = len(grid), len(grid[0])
        if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] == '0':
            return

        grid[i][j] = '0'
        self.dfs(grid, i + 1, j )
        self.dfs(grid, i - 1, j)
        self.dfs(grid, i, j + 1)
        self.dfs(grid, i, j - 1)

    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    count += 1
                    self.dfs(grid, i, j)
        return count












"""
Approach:
Traversal Strategy:
    Use either Depth-First Search (DFS) or Breadth-First Search (BFS) to explore each island starting from a '1'.
    Mark visited cells to avoid recounting.
Implementation Steps:
    Iterate through all cells in the grid.
    When a cell with '1' is found, increment the island count and start a DFS/BFS to mark all connected land cells as visited.
    Continue until all cells are processed.
Edge Cases:
    Grid with all '0's (output: 0 islands).
    Grid with all '1's (output: 1 island).


"""
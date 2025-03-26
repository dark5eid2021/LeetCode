class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        visited = set()
        rows, cols = len(grid), len(grid[0])

        def bfs(r, c):
            q = deque()
            visited.add((r, c))
            q.append((r, c))

            while q:
                row, col = q.popleft()
                directions = [[1,0],[-1,0],[0,1],[0,-1]]

                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if 0 <= r < rows and 0 <= c < cols and grid[r][c] == "1" and (r, c) not in visited:
                        q.append((r, c))
                        visited.add((r, c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    islands += 1
                    bfs(r, c)

        return islands
    


"""
The BFS approach involves using a queue to systematically explore all cells of each island. We'll iterate through each cell in the grid. When encountering a '1' (indicating land), we'll use BFS to explore all connected land cells and mark them as visited.

BFS Function: Use a queue to perform BFS starting from each unvisited land cell ('1').

Initialize a queue with the starting cell.
While the queue is not empty, dequeue a cell, mark it as visited, and enqueue its neighboring land cells (up, down, left, right).
Continue until all connected land cells of the current island are visited.
Main Function:

Iterate through each cell in the grid.
If encountering an unvisited '1', increment the island count and trigger BFS to explore and mark all connected land cells of this island.


"""
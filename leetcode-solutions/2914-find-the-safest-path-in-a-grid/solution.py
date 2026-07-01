from collections import deque

class Solution(object):
    def __init__(self):
        self.dir = [(0,1), (1,0), (0,-1), (-1,0)]

    def maximumSafenessFactor(self, grid):
        n = len(grid)

        # -----------------------------
        # Step 1: Multi-source BFS
        # -----------------------------
        multi_source_queue = deque()

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    multi_source_queue.append((i, j))
                    grid[i][j] = 0
                else:
                    grid[i][j] = -1

        while multi_source_queue:
            r, c = multi_source_queue.popleft()

            for dr, dc in self.dir:
                nr, nc = r + dr, c + dc

                if self.isValidCell(grid, nr, nc) and grid[nr][nc] == -1:
                    grid[nr][nc] = grid[r][c] + 1
                    multi_source_queue.append((nr, nc))

        # -----------------------------
        # Step 2: Binary Search
        # -----------------------------
        start = 0
        end = 0

        for row in grid:
            end = max(end, max(row))

        ans = 0

        while start <= end:
            mid = (start + end) // 2

            if self.isValidSafeness(grid, mid):
                ans = mid
                start = mid + 1
            else:
                end = mid - 1

        return ans

    # -----------------------------
    # Check valid cell
    # -----------------------------
    def isValidCell(self, grid, i, j):
        n = len(grid)
        return 0 <= i < n and 0 <= j < n

    # -----------------------------
    # BFS to check if path exists
    # -----------------------------
    def isValidSafeness(self, grid, minSafeness):
        n = len(grid)

        if grid[0][0] < minSafeness or grid[n-1][n-1] < minSafeness:
            return False

        q = deque([(0, 0)])
        visited = [[False] * n for _ in range(n)]
        visited[0][0] = True

        while q:
            r, c = q.popleft()

            if r == n - 1 and c == n - 1:
                return True

            for dr, dc in self.dir:
                nr, nc = r + dr, c + dc

                if (self.isValidCell(grid, nr, nc)
                        and not visited[nr][nc]
                        and grid[nr][nc] >= minSafeness):

                    visited[nr][nc] = True
                    q.append((nr, nc))

        return False

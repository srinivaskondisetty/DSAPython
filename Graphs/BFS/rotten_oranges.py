from typing import List
from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        result, fresh = 0, 0
        m, n = len(grid), len(grid[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        queue = deque()
        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                if grid[i][j] == 2:
                    queue.append([i, j])
                if grid[i][j] == 1:
                    fresh += 1

        while queue and fresh > 0:
            for i in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in directions:
                    row, col = r + dr, c + dc

                    if ((row < 0 or row == m or col < 0 or col == n) or grid[row][col] != 1):
                        continue
                    grid[row][col] = 2
                    queue.append([row, col])
                    fresh -= 1
            result += 1
        return result if fresh == 0 else -1


solution = Solution()
result = solution.orangesRotting([[0,2]])
print('result', result)
class Solution:
  def maxDistance(self, grid: List[List[int]]) -> int:
    n = len(grid)
    stack = [[0] * n for _ in range(n)]

    for i in range(n):
      for j in range(n):
        if grid[i][j] == 0:
          top = stack[i - 1][j] if i else inf
          left = stack[i][j - 1] if j else inf
          stack[i][j] = min(top, left) + 1

    for i in range(n - 1, -1, -1):
      for j in range(n - 1, -1, -1):
        if grid[i][j] == 0:
          bottom = stack[i + 1][j] if i + 1 < n else inf
          right = stack[i][j + 1] if j + 1 < n else inf
          stack[i][j] = min(stack[i][j], bottom + 1, right + 1)

    answer = max(max(row) for row in stack)
    return -1 if answer in (0, inf) else answer

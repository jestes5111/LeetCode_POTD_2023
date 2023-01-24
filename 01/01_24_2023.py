class Solution:
  def snakesAndLadders(self, board: List[List[int]]) -> int:
    n = len(board)

    def get_position(i: int) -> (int, int):
      row, column = divmod(i - 1, n)
      if row % 2 == 0: return (n - 1 - row), column
      return (n - 1 - row), (n - 1 - column)

    seen = set()
    queue = collections.deque()
    queue.append((1, 0))
    while queue:
      label, step = queue.popleft()
      row, column = get_position(label)
      if board[row][column] != -1: label = board[row][column]
      if label == n * n: return step

      for i in range(1, 7):
        new_label = label + i
        if new_label <= n * n and new_label not in seen:
          seen.add(new_label)
          queue.append((new_label, step + 1))
      
    return -1

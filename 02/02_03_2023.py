class Solution:
  def convert(self, s: str, numRows: int) -> str:
    if numRows == 1: return s

    rows = [''] * numRows
    index = 1
    goingUp = True

    for c in s:
      rows[index - 1] += c
      if index == numRows:
        goingUp = False
      elif index == 1:
        goingUp = True
      index = index + 1 if goingUp else index - 1

    return ''.join(rows)

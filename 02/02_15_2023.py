class Solution:
  def addToArrayForm(self, num: List[int], k: int) -> List[int]:
    new_num = int(''.join(map(str, num))) + k
    return list(map(int, str(new_num)))

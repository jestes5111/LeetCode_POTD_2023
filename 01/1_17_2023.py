class Solution:
  def minFlipsMonoIncr(self, s: str) -> int:
    if '0' not in s or '1' not in s: return 0

    answer = ones = 0
    for c in s:
      if c == '1': 
        ones += 1
      elif ones:
        ones -= 1
        answer += 1
    return answer

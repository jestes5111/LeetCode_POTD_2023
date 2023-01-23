class Solution:
  def findJudge(self, n: int, trust: List[List[int]]) -> int:
    if not trust: return 1 if n == 1 else -1

    trusted = [0] * (n + 1)
    for a, b in trust:
      trusted[a] -= 1
      trusted[b] += 1
    
    for person in trusted:
      if person == (n - 1): return trusted.index(person)
    return -1

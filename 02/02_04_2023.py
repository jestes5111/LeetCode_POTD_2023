class Solution:
  def checkInclusion(self, s1: str, s2: str) -> bool:
    center, window, match = Counter(s1), len(s1), 0
    
    for i in range(len(s2)):
      if s2[i] in center:
        center[s2[i]] -= 1
        if center[s2[i]] == 0: match += 1
      
      if i >= window and s2[i - window] in center:
        if center[s2[i - window]] == 0: match -= 1
        center[s2[i - window]] += 1
      
      if match == len(center): return True
    return False

class Solution:
  def distinctNames(self, ideas: List[str]) -> int:
    first = defaultdict(set)
    for idea in ideas:
      first[ord(idea[0]) - ord('a')].add(idea[1:])
    
    names = 0
    for i in range(25):
      for j in range(i + 1, 26):
        k = len(first[i] & first[j])
        names += 2 * (len(first[i]) - k) * (len(first[j]) - k)
    return names

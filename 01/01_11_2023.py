class Solution:
  def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
    seen = set()
    m = defaultdict(list)

    for a, b in edges:
      m[a].append((b))
      m[b].append((a))

    def dfs(node: int) -> int:
      seen.add(node)
      answer = sum(dfs(n) for n in m[node] if n not in seen)
      if not answer and not hasApple[node]: return 0
      return answer + 2
    
    return max(0, dfs(0) - 2)

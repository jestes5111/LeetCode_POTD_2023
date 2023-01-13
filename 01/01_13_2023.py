class Solution:
  def longestPath(self, parent: List[int], s: str) -> int:
    tree = defaultdict(list)
    for end, start in enumerate(parent):
      tree[start].append(end)
    
    answer = 1

    def dfs(node: int) -> int:
      nonlocal answer
      a = b = 0
      for neighbor in tree[node]:
        longest = dfs(neighbor)

        if s[neighbor] == s[node]: continue

        if longest > a:
          b, a = a, longest
        elif longest > b:
          b = longest
      
      answer = max(answer, a + b + 1)
      return a + 1
    
    dfs(0)
    return answer

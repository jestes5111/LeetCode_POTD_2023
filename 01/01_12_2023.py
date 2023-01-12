class Solution:
  def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
    graph = defaultdict(list)
    label_count = defaultdict(int)
    answer = [0] * n

    for a, b in edges:
      graph[a].append(b)
      graph[b].append(a)

    def dfs(node: int, parent: int) -> None:
      previous = label_count[labels[node]]
      label_count[labels[node]] += 1

      for child in graph[node]:
        if child != parent: dfs(child, node)

      answer[node] = label_count[labels[node]] - previous

    dfs(0, None)
    return answer
